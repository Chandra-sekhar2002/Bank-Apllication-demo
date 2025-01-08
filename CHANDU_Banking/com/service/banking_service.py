#from CHANDU_Banking.com.app import user_mail
from CHANDU_Banking.com.repo.db_operations import *
from CHANDU_Banking.com.service.mail_operations import *

# function to fetch userId based on user_email
def fetch_userID(user_mail):

    # fetching entire row based on email from chandu_users
    db_data_users = fetch_data('chandu_users', email=user_mail)
    try:
        # fetching userId variable from entire row
        userId = db_data_users[0][0]
        return userId

    except:
        return False


def displayBalance(user_mail):

    #fetching userId based on user_mail from chandu_users table
    userId = fetch_userID(user_mail)

    if userId:
        db_data_accounts = fetch_data('chandu_accounts', user_id=userId)
        print("[+] Account Balance: " + str(db_data_accounts[0][3]))
        print()
        return True

    else:
        return False


def depositMoney(user_mail,depositAmount):

    # fetching userId based on user_mail from flm_users table
    userId = fetch_userID(user_mail)

    if userId:
        try:
            # fetching entire row of chandu_accounts table based on userId
            db_data_accounts = fetch_data('chandu_accounts', user_id=userId)

            # extracting and updating balance variable from entire row
            balance = db_data_accounts[0][3] + depositAmount

            # updating balance variable in database, chandu_accounts table using userId
            update_data('chandu_accounts', values={'balance': balance}, conditions={'user_id': userId})
            displayBalance(user_mail)

            return True

        except:

            return False
    else:

        return False

def withdrawlMoney(user_mail,withdrawlMoney):

    # fetching userId based on user_mail from flm_users table
    userId = fetch_userID(user_mail)

    if userId:

        # fetching entire row of chandu_accounts table based on userId
        db_data_accounts = fetch_data('chandu_accounts', user_id=userId)

        # extracting user balance from entire row data
        balance = db_data_accounts[0][3]

        # function to check whether user balance is greater than withdrawlamount
        if balance > withdrawlMoney:
            balance = balance - withdrawlMoney

            # updating new user balance into database
            update_data('chandu_accounts', values={'balance': balance}, conditions={'user_id': userId})
            displayBalance(user_mail)
            return True

        else:
            print("[-] Insufficient Funds...")
            print()
            return False

    else:
        return False


def transferMoney(user_mail,transferAmount):

    # fetching senderUserId based on user_mail from chandu_users table
    senderUserId = fetch_userID(user_mail)

    # fetching account information from senderUserId from chandu_accounts table
    senderAccountDetails = fetch_data('chandu_accounts', user_id=senderUserId)

    # extracting senderDetails from chandu_accounts table
    senderBalance = senderAccountDetails[0][3]
    senderAccountId = senderAccountDetails[0][0]
    senderAccountNumber = senderAccountDetails[0][2]

    # checking whether senderBalance is greater than amount to be transferred
    if senderBalance > transferAmount:

        # receiver accountId
        receiverAccountId = int(input("Enter Recepients Account Id: "))
        #account_ids = fetch_column_data('chandu_accounts', 'account_id')

        # checking whether receiver account does exist or not
        if receiverAccountId in fetch_column_data('chandu_accounts', 'account_id'):

            # performing update operations on sender account balance
            UptSenderBalance = senderBalance - transferAmount

            # updating new sender account info into chandu_accounts database
            update_data('chandu_accounts', values={'balance': UptSenderBalance}, conditions={'user_id': senderUserId})
            displayBalance(user_mail)

            # fetching receiver account info from chandu_accounts
            receiver_db_data = fetch_data('chandu_accounts', account_id=receiverAccountId)

            # extracting receiver data
            receiverUserId = receiver_db_data[0][1]
            receiverAccountNumber = receiver_db_data[0][2]

            # performing update operations on receiver account balance
            receiverBalance = receiver_db_data[0][3] + transferAmount

            # updating receiver account info into database
            update_data('chandu_accounts', values={'balance': receiverBalance}, conditions={'account_id': receiverAccountId})



            # inserting transaction details into chandu_transactions table (sender side)
            insert_data('chandu_transactions', user_id=senderUserId, account_id=senderAccountId, amount=transferAmount, from_account=senderAccountNumber,
                        to_account=receiverAccountNumber, trans_type='db')


            # inserting transaction details into chandu_transactions table (sender side)
            insert_data('chandu_transactions', user_id=receiverUserId, account_id=receiverAccountId, amount=transferAmount,
                        from_account=senderAccountNumber,
                        to_account=receiverAccountNumber,trans_type='cd')

            return True

        else:
            print("[-] Receiver Account Do not exist..")
            print()
            return False

    else:
        print("[-] Insufficient Balance..")
        print()
        return False

def transactionHistory(user_email):
    try:
        # Connect to the MySQL database
        conn = db_connect()

        # Create a cursor to execute SQL queries
        cursor = conn.cursor()

        # Query to retrieve transaction history based on user email
        query = """
                SELECT chandu_users.first_name, chandu_users.last_name, chandu_accounts.account_number, chandu_transactions.amount, chandu_transactions.from_account, chandu_transactions.to_account, chandu_transactions.trans_date, chandu_transactions.trans_type
                FROM chandu_users
                INNER JOIN chandu_transactions ON chandu_users.user_id = chandu_transactions.user_id
                INNER JOIN chandu_accounts ON chandu_transactions.account_id = chandu_accounts.account_id
                WHERE chandu_users.email = %s
            """

        # Execute the query with the provided user_email
        # Execute the query and fetch transaction history
        cursor.execute(query, (user_email,))

        # Initialize the message string
        message = f"Transaction History for User: {user_email}\n\n"
        message += "{:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<10}\n".format(
            "First Name", "Last Name", "Account Number", "Amount", "From Account", "To Account", "Date", "Trans Type"
        )
        message += "-" * 100 + "\n"

        # Fetch rows and append to the message
        for row in cursor.fetchall():
            first_name, last_name, account_number, amount, from_account, to_account, trans_date, trans_type = row
            message += "{:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<10}\n".format(
                first_name, last_name, account_number, amount, from_account, to_account, str(trans_date), trans_type
            )

        # Print the message (for debugging purposes)
        print(message)

        # You can now send this `message` via email or other communication methods

        statement_sent_to(email=user_email,statement=message)
        print()
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        return True

    except mysql.connector.Error as e:
        #
        # baprint("Error:", e)
        return False





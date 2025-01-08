def fancy(n):
    result=str(n)
    def tofancy(a):
        res=""
        res+=str(n*a)
        return res
    result+=str(tofancy(i))
    for i in range(1,10-len(n)):
         if len(result)>10:
          break
print(fancy(n=192))






import time
gk = lambda i,j:str(i)+','+str(j)

def optimal_BST(p, q, n):   
    MAX = (max(p)>max(q) and max(p) or max(q))*(n+1)*(len(p)+len(q)) 
    e, w, root = {}, {}, {} 
    for i in range(1, n+2): 
        e[gk(i, i-1)] = q[i-1]
        w[gk(i, i-1)] = q[i-1]
    for l in range(1, n+1): 
        for i in range(1, n-l+2):
            j = i+l-1      
            e[gk(i, j)] = MAX
            w[gk(i, j)] = w[gk(i, j-1)]+p[j-1]+q[j]
            for r in range(i, j+1):
                t = e[gk(i, r-1)]+e[gk(r+1, j)]+w[gk(i, j)]
                if t<e[gk(i, j)]:
                    e[gk(i, j)] = t
                    root[gk(i, j)] = r
    print("e array is :\n")
    for r1 in e:
        print(r ,":" ,e[r1])
    print("\n\n\n")
    print("w array is :\n")
    for r2 in e:
        print(r ,":" ,w[r2])
    print("\n\n\n")
    print("root array is :\n")
    print(root)
    return e, root

p = [      0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]
e, root = optimal_BST(p, q, len(p))
print ("\noptimal cust of the tree is:" , e[gk(1,len(p))])

input()

# code written by Yasin Boloorchi. 
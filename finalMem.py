def fifo(frames,pages):
    n=len(frames)
    m=len(pages)
    hit=0
    fault=0
    for i in range(m):
        if pages[i] not in frames:
            fault+=1
            frames.pop(0)
            frames.append(pages[i])
            print(f" {pages[i]} added toh frames")
            print("fault")
        else :
            hit+=1
            print("hit")
        print(f" current frames {frames}")

def lru(frames,pages):
    n=len(frames)
    m=len(pages)
    hit=0
    fault=0
    dict={}
    for page in pages:
        if page not in dict:
            if len(dict)==n:
                to_remove=sorted(dict.items(),key=lambda x:(x[1]))[0][0]
                del dict[to_remove]
                fault+=1
                print("fault")
            dict[page]=0
            if len(dict)<n:
                print("fault")
                fault+=1
        else:
            dict[page]=0
            print("hit")
            hit+=1
            
        for p in dict:
            if p!=page:
                dict[p]+=1
        print(f"page {page} added to frames")
        print(f"current frames are {dict.items()}")


n=int(input("enter frames"))
m=int(input("enter no of pages"))
print("enter pages")
pages=[]
for _ in range(m):
    pages.append(input())
frames=[None]*n
fifo(frames,pages)
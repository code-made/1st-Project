import json, os
F="todo_tasks.json"

def load():
    if os.path.exists(F):
        try:
            return json.load(open(F))
        except Exception:
            pass
    return []

def save(t):
    try:
        json.dump(t, open(F,"w"), indent=2)
    except Exception as e:
        print("Error saving:", e)

def seed(t):
    t[:] = [
        {"id": 1, "task": "Learn Coding", "completed": False},
        {"id": 2, "task": "Reading books", "completed": True},
        {"id": 3, "task": "Write report", "completed": False},
    ]
    save(t)
    print("Seeded 3 tasks.")

def reset(t):
    t.clear()
    save(t)
    print("Reset tasks.")

def nid(t): return max((x["id"] for x in t), default=0)+1
def pause(): input("\nEnter to continue...")

def show(t):
    if not t: print("\nNo tasks."); return
    print("\nTasks:")
    for x in t:
        print(f"[{x['id']:>3}] {'✅' if x.get('completed') else '⏳'} {x['task']}")

def add(t):
    s=input("\nTask: ").strip()
    if s: t.append({"id":nid(t),"task":s,"completed":False}); save(t); print("Added.")
    else: print("Empty ignored.")

def upd(t):
    show(t)
    try: i=int(input("\nUpdate ID: "))
    except: print("Invalid ID."); return
    x=next((y for y in t if y["id"]==i),None)
    if not x: print("Not found."); return
    s=input("New text: ").strip()
    if s: x["task"]=s; save(t); print("Updated.")
    else: print("Empty ignored.")

def done(t):
    show(t)
    try: i=int(input("\nComplete ID: "))
    except: print("Invalid ID."); return
    x=next((y for y in t if y["id"]==i),None)
    if not x: print("Not found."); return
    x["completed"]=True; save(t); print("Completed.")

def rm(t):
    show(t)
    try: i=int(input("\nDelete ID: "))
    except: print("Invalid ID."); return
    n=len(t); t[:]=[y for y in t if y["id"]!=i]
    if len(t)<n: save(t); print("Deleted.")
    else: print("Not found.")

def stat(t):
    n=len(t); d=sum(x["completed"] for x in t); p=n-d; k=(d*100//n) if n else 0
    print(f"\nStats: Total={n}, Completed={d}, Pending={p}, Progress={k}%")
    print("All done! 🎉" if k==100 else "Almost there! 🚀" if k>=75 else "Keep it up! 💪" if k>=50 else "Making progress! 🔄" if k>=25 else "Just getting started! 🌱")

def menu():
    print("\n--- TODO ---\n1) Add\n2) View\n3) Stats\n4) Update\n5) Complete\n6) Delete\n7) Exit\n8) Reset\n")

def main():
    t=load(); print("Welcome to Todo!")
    m={"0":seed,"1":add,"2":lambda x:(show(x),None),"3":stat,"4":upd,"5":done,"6":rm,"8":reset}
    while True:
        menu(); c=input("Choose (1-8): ").strip()
        if c=="7": print("Bye!"); break
        (m.get(c) or (lambda *_:print("Invalid.")))(t); pause()

if __name__=="__main__": main()

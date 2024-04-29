import time
import secrets

def waiting_game():
    target=secrets.SystemRandom().randint(2,4)
    print(f"please wait {target} time and then press enter ")
    input("please presse enter to begin")
    timer=time.perf_counter()
    input(f"please press enter again after{target} seconds")
    elapsed = time.perf_counter() - timer
     
    if elapsed == target:
         print(f"Elapsed time:{elapsed} seconds perfect timing!!")
    elif elapsed > target:
        print(f"Elapsed time:{target - elapsed :.3f} seconds too fast")
    elif elapsed< target:
        print(f"Elapsed time:{elapsed-target  :.3f} seconds too slow")


# commands used in solution video for reference
if __name__ == '__main__':
    waiting_game()

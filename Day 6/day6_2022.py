"""The one with the n distinct characters"""

def solve(n):
    for i in range(0,len(signal)):
        packet = signal[i:i+n]
        if len(set(packet)) == n:
            return i+n

with open('input.txt','r') as f:
    signal = f.read().strip()

    print(f"First result: {solve(4)}")
    print(f"Second result: {solve(14)}")

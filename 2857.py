import re

agents = [input().strip() for _ in range(5)]

pattern = r'^[A-Z0-9-]{1,10}$'

fbi_agent = [i + 1 for i, agent in enumerate(agents) if re.match(pattern, agent) and 'FBI' in agent]

if fbi_agent:
    print(" ".join(map(str, fbi_agent)))
else:
    print("HE GOT AWAY!")
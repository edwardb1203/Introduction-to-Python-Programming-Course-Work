"""Viral Calculator"""
__author__ = "730312903"
R0: str = input("Enter R0: ")
t0: str = input("Enter t0 Cluster size: ")
Viral_Growth_Rate = (float(R0))
Cluster_Size = int(t0)
time_elapsed: int = 2
infection_size: int = 1
Newly_Infected: int = round(int(Viral_Growth_Rate ** (time_elapsed-1) * Cluster_Size))
Previous_infected: int = round(int(Viral_Growth_Rate ** (time_elapsed-1) * Cluster_Size) + Newly_Infected * (infection_size-1))
Total_infections: int = round(int(Cluster_Size + Previous_infected))
print("t" + str(time_elapsed-1) + " - New: " + str(Newly_Infected) + " - Total: " + str(Total_infections))
time_elapsed: int = 3
infection_size: int = 2
Newly_Infected: int = round(int(Viral_Growth_Rate ** (time_elapsed-1) * Cluster_Size))
Previous_infected: int = round(int(Viral_Growth_Rate ** (time_elapsed-1) * Cluster_Size) + Newly_Infected * (infection_size-1))
Total_infections: int = round(int(Cluster_Size + Previous_infected))
print("t" + str(time_elapsed-1) + " - New: " + str(Newly_Infected) + " - Total: " + str(Total_infections))


other idea for Previous_infected: int = round(int(Newly_Infected + (Viral_Growth_Rate ** (time_elapsed-1) * (infection_size-1))))
and have Total_infections: int = round(int(Newly_Infected + Cluster_Size + Previous_infected))
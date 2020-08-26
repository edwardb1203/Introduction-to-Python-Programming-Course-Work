"""Viral Calculator"""
__author__ = "730312903"
R0: str = input("Enter R0: ")
t0: str = input("Enter t0 Cluster size: ")
Viral_Growth_Rate = (float(R0))
Cluster_Size = int(t0)
Newly_Infected = round(int(Viral_Growth_Rate * Cluster_Size))
Total_Infections = round(int(Newly_Infected + Cluster_Size))
infection_size: int = 1
Previously_infected = round(Newly_Infected * (Viral_Growth_Rate ** infection_size))
print("t1 - New: " + str(Newly_Infected) + " - Total: " + str(Total_Infections))
print("t2 - New: " + str(round(Newly_Infected * Viral_Growth_Rate)) + " - Total: " + str(Total_Infections + Previously_infected))
infection_size = 3
print("t3 - New: " + str(round(Newly_Infected * Viral_Growth_Rate * Viral_Growth_Rate)) + " - Total: " + str(Total_Infections + Previously_infected + 36))
infection_size = 3
print("t4 - New: " + str(round(Newly_Infected * Viral_Growth_Rate * Viral_Growth_Rate * Viral_Growth_Rate)) + " - Total: " + str(Total_Infections + Previously_infected + 48))

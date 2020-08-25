"""Viral Calculator"""
_author_ = "730312903"
R0: str = input("Enter R0: ")
t0: str = input("Enter t0 Cluster size: ")
Viral_Growth_Rate = (float(R0))
Cluster_Size = int(t0)
Newly_Infected = round(int(Viral_Growth_Rate * Cluster_Size))
Total_Infections = round(int(Newly_Infected + Cluster_Size))
print ("t1 - New: " + str(Newly_Infected) + " - Total: " + str(Total_Infections))
print ("t2 - New: " + str(round(Newly_Infected * Viral_Growth_Rate)) + " - Total: " + str(Total_Infections + round(Newly_Infected * Viral_Growth_Rate)))
print ("t3 - New: " + str(round(Newly_Infected * Viral_Growth_Rate * Viral_Growth_Rate)) + " - Total: " + str(Total_Infections + round(Newly_Infected * Viral_Growth_Rate * Viral_Growth_Rate) + round(Newly_Infected * Viral_Growth_Rate)))
print ("t4 - New: " + str(round(Newly_Infected * Viral_Growth_Rate * Viral_Growth_Rate * Viral_Growth_Rate)) + " - Total: " + str(Total_Infections + round(Newly_Infected * Viral_Growth_Rate * Viral_Growth_Rate * Viral_Growth_Rate) + round(Newly_Infected * Viral_Growth_Rate * Viral_Growth_Rate) + round(Newly_Infected * Viral_Growth_Rate)))

"""Viral Calculator!"""
__author__ = "730312903"
R0: str = input("Enter R0: ")
t0: str = input("Enter t0 Cluster size: ")
Viral_Growth_Rate = (float(R0))
Cluster_Size = int(t0)
time_elapsed: int = 2
Newly_Infected: int = round(float(Viral_Growth_Rate ** float((time_elapsed - 1)) * Cluster_Size))
Previous_infected: int = round(int((Viral_Growth_Rate ** (time_elapsed - 1)) * Cluster_Size))
Total_infections: int = round(int(Cluster_Size + Previous_infected))
print("t" + str(time_elapsed - 1) + " - New: " + str(Newly_Infected) + " - Total: " + str(Total_infections))
time_elapsed += 1
Newly_Infected: int = round(float(Viral_Growth_Rate ** float((time_elapsed - 1)) * float(Cluster_Size)))
Previous_infected = Total_infections
Total_infections = round(int(Newly_Infected + Previous_infected))
print("t" + str(time_elapsed - 1) + " - New: " + str(Newly_Infected) + " - Total: " + str(Total_infections))
time_elapsed += 1
Newly_Infected: int = round(float(Viral_Growth_Rate ** float((time_elapsed - 1)) * float(Cluster_Size)))
Previous_infected = Total_infections
Total_infections = round(int(Newly_Infected + Previous_infected))
print("t" + str(time_elapsed - 1) + " - New: " + str(Newly_Infected) + " - Total: " + str(Total_infections))
time_elapsed += 1
Newly_Infected: int = round(float(Viral_Growth_Rate ** float((time_elapsed - 1)) * float(Cluster_Size)))
Previous_infected = Total_infections
Total_infections = round(int(Newly_Infected + Previous_infected))
print("t" + str(time_elapsed - 1) + " - New: " + str(Newly_Infected) + " - Total: " + str(Total_infections))


import matplotlib
matplotlib.use('agg')  # Use this backend or try 'Qt5Agg' if TkAgg doesn't work
import pandas as pd
import matplotlib.pyplot as plt

# Print graph
data = {"Year": [2010, 2011, 2012, 2013, 2014],
        "Sales": [500, 600, 750, 800, 900]}
df = pd.DataFrame(data)

df.plot(x="Year", y="Sales", marker="o", linestyle='-', color='b',label="Sales")

plt.savefig("sales_plot.png")

# Print bara graph
# data = {"Year": [2010, 2011, 2012, 2013, 2014],
#         "Sales": [500, 600, 750, 800, 900]}
# df = pd.DataFrame(data)
#
# df.plot(x="Year", y="Sales", kind="bar", color='b',label="Sales")
# plt.xlabel("Year")
# plt.ylabel("Sales")
# plt.title("Sales per Year")
# plt.legend()
# plt.grid(True)
#
# plt.show()

# Print histogram
# data = {"Year": [2010, 2011, 2012, 2013, 2014],
#         "Sales": [500, 600, 750, 800, 900]}
# df = pd.DataFrame(data)
#
# df.plot(x="Year", y="Sales", kind="hist", color='b',label="Sales")
# plt.xlabel("Year")
# plt.ylabel("Sales")
# plt.title("Sales per Year")
# plt.legend()
# plt.grid(True)
#
# plt.show()

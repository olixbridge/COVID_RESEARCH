
import geopandas as gp
import matplotlib.pyplot as plt

#sa2 = gpd.read_file( os.path.join(data_path, "gpr_000b11a_e.shp") )
#sa2 = sa2.drop(columns = ['MB_CODE16', 'MB_CAT16','SA2_NAME16', 'SA1_MAIN16', 'SA1_7DIG16','SA4_NAME16', 'STE_CODE16', 'SA2_5DIG16', 'SA3_CODE16', 'SA3_NAME16', 'SA4_CODE16', 'GCC_CODE16', 'GCC_NAME16', 'STE_NAME16', 'AREASQKM16'])
#sa2

shp = gp.GeoDataFrame.from_file("/Users/oliviashi/Documents/french/research_master/gpr_000b11a_e/gpr_000b11a_e.shp")
print(shp)


fig, ax = plt.subplots(figsize = (10,10))
shp.plot(ax=ax)
plt.show()
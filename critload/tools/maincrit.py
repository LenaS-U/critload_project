import os
import sys
import traceback

import general_path
from iround import *
from error import *
import ascraster
import my_sys

file1 = os.path.join('d:', os.sep, 'project', 'generalcode','testgrid10.asc')
print(file1)

# Add grid1 with a scalar of type float
# Read ascii grid
grid1 = ascraster.Asciigrid(ascii_file=file1,numtype=int)
factor = 4
grid1_old = ascraster.duplicategrid(grid1)
grid1.add(factor)
print(grid1_old.values)
print(grid1.values)
	
grid1.substract(factor)
print(grid1_old.values)
print(grid1.values)

print("the number of coloumns is", grid1.ncols)
print("the number of coloumns is " + str(grid1.ncols))
print("the number of rows is " + str(grid1.nrows))
print("the xll corner is " + str(grid1.xllcorner))
print("the length of the raster is " + str(grid1.length))
print(grid1.get_data(6))
grid1.set_data(6,3)
print(grid1.get_data(6))
grid1.set_data(6,grid1.nodata_value)
print(grid1.get_data(6,100))
print(grid1.nodata_value)

def const_grid (grid, val):
	for icell in range(grid.length):
		grid.set_data(icell,val)


icell_debug=3

def print_debug (grid, txt):
	if (icell_debug > -1):
		print(txt + " " + str(grid.get_data(icell_debug)))



for icell in range(grid1.length):
	val=grid1.get_data(icell)
	if (val != None):
		print(iround(icell), iround(val))		

if (__name__ == "__main__"):
	try:
		file1 = os.path.join('d:', os.sep, 'project', 'generalcode','testgrid100.asc')
		inpdir = os.path.join('d:', os.sep, 'project', 'critload','input')
		
		#a_tot = ascraster.Asciigrid(ascii_file=os.path.join(inpdir,'a_tot.asc'),numtype=float)
		#a_ag = ascraster.Asciigrid(ascii_file=os.path.join(inpdir,'a_ag.asc'),numtype=float)
		#a_ag.divide(a_tot)
		#fileout = r"..\input\fag.asc"
		#a_ag.write_ascii_file(fileout)
		#print_debug(a_ag,"is de waarde voor fag")
		
        #write value to grid
		val = 500000
		const_grid(grid1,val)
		
		fileout = r"..\input\nfix_ag.asc"
		grid1.write_ascii_file(fileout)
		print_debug(grid1,"dit is een test")
		
		
		
		try:
			fp= open (file1, 'r')
		except: 
			raise MyError ("Lena is leuk")
			
		grid1 = ascraster.Asciigrid(ascii_file=file1,numtype=int)
	except MyError as val:
		val.write()
		
	except:
		print("***** ERRROR ****")
		print("allocation.py failed.")
		print(str(sys.exc_info())[0])
		print(traceback.print_exc())
		
		
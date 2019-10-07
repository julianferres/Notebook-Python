from math import *

def gratCircleDistance( pLat, pLong, qLat, qLong, radius ):
	
	pLat *= pi/180
	pLong *= pi/180
	qLat *= pi/180
	qLong *= pi/180
	
	return radius*acos(cos(pLat)*cos(pLong)*cos(qLat)*cos(qLong)+
						cos(pLat)*sin(pLong)*cos(qLat)*sin(qLong)+
						sin(pLat)*sin(qLat))

	
	

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:09:10 2020

@author: alanna genin
"""

# XXX -- Top level review comments:
#
# * Nice exception recovery and logging.
#
# * Please cleanup code formatting.
#   This is a little rough on my eyes.
#
# * Should we use this as template for other
#   short network element scripts?
#
# -- Thanks.   The Boss :-) 

import jnettool.tools.elements.NetworkElement, \
       jnettool.tools.Routing, \
       jnettool.tools.RouteInsector

ne=jnettool.tools.elements.NetworkElement( '171.0.2.45' )
try:
    routing_table=ne.getRoutingTable()  # fetch table

except jnettool.tools.elements.MissingVar:
  # Record table fault
  logging.exception( '''No routing table found''' )
  # Undo partial changes
  ne.cleanup( '''rollback''' )

else:
    num_routes=routing_table.getSize()   # determine table size
    for RToffset in range ( num_routes ):
           route=routing_table.getRouteByIndex( RToffset )
           name=route.getName()       # route name
           ipaddr=route.getIPAddr()          # ip address
           print("%15s -> %s"% (name,ipaddr)) # format nicely
finally:
    ne.cleanup( '''commit''' ) # lockin changes
    ne.disconnect()


#----------------------------------- Better -----------------------------------
        
import jnettool.tools.elements.NetworkElement
import jnettool.tools.Routing
import jnettool.tools.RouteInsector

ne = jnettool.tools.elements.NetworkElement('171.0.2.45')

try:
	routing_table = ne.getRoutingTable()
except jnettool.tools.elements.MissingVar:
	logging.exception('No routing table found')
	ne.cleanup('rollback')
else:
	num_routes = routing_table.getSize() 
	for RToffset in range(num_routes):
		route = routing_table.getRouteByIndex(RToffset)
		name = route.getName()
		ipaddr = route.getIPAddr()
		print("%15s -> %s" % (name, ipaddr))
finally:
	ne.cleanup('commit')
	ne.disconnect()
    
#----------------------------------- Testing ----------------------------------
    
from nettools import NetworkElement

with NetworkElement('171.0.2.45') as ne:
	for route in ne.routing_table:
		print("%15s -> %s" % (route.name, route.ipaddr))

#------------------------------------------------------------------------------
                
''' Pythonic means "coding beautifully in harmony with
    the language to get the maximum benefits from Python"
    Learn to recognize non-pythonic APIs and to recognize
    good code.  Don't get distracted by PEP 8.  Focus
    first an Pythonic versus NonPython (P vs NP).
    When needed, write an adapter class to convert from
    the former to the latter.
    * Avoid unnecessart packageing in favor of 
      simpler imports
    * Create custom exceptions
    * Use properties instaed of getter methods
    * Create a context manager for recurring
      set-up and teardown logic
    * Use magic methods:
          __len__ instead of getSize()
          __getitem__ instead of getRouteByIndex()
          make the table iterable
    * Add good __repr__ for better dubuggability
'''

######################## Adapter ########################

import jnetool.tools.elements.NetworkElement
import jnetool.tools.Routing

class NetworkElementError(Exception):
    pass

class NetworkElement(object):

    def __init__(self, ipaddr):
        self.ipaddr = ipaddr
        self.oldne = jnetool.tools.elements.NetworkElement(ipaddr)

    @property
    def routing_table(self):
        try:
            return RoutingTable(self.oldne.getRoutingTable())
        except jnetool.tools.elements.MissingVar:
            raise NetworkElementError('No routing table found')

    def __enter__(self):
        return self

    def __exit__(self, exctype, excinst, exctb):
        if exctype == NetworkElementError:
            logging.exception('No routing table found')
            self.oldne.cleanup('rollback')
        else:
            self.oldne.cleanup('commit')
        self.oldne.disconnect()

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.ipaddr)


class RoutingTable(object):

    def __init__(self, oldrt):
        self.oldrt = oldrt

    def __len__(self):
        return self.oldrt.getSize()

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        return Route(self.oldrt.getRouteByIndex(index))


class Route(object):

    def __init__(self, old_route):
        self.old_route = old_route

    @property
    def name(self):
        return self.old_route.getName()

    @property
    def ipaddr(self):
        return self.old_route.getIPAddr()
    
 
    #------------------------------------------------------------------------------

    
twitter_search('obama', numtweets=20, retweets=False, unicode=True)

from collections import namedtuple

Color = namedtuple('Color', ['hue', 'saturation', 'luminosity'])

#before
p = (170, 0.1, 0.6)
if p[1] >= 0.5:
    print('Whew, that is bright!')
if p[2] >= 0.5:
    print('Wow, that is light')
    
#after    
p = (170, 0.1, 0.6)
if p.saturation >= 0.5:
    print('Whew, that is bright!')
if p.luminosity >= 0.5:
    print('Wow, that is light')

def get_routes(*symbols):
    'Return a dictionary of real-time stock quotes'
    return {symbol: get_quote(symbol for symbol in symbols)}


for interface, status in interfaces:
    if status.lower() == 'up':
        print(interface)
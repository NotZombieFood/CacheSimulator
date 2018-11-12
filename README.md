# cache tables
## Created for education oriented stuff, this library will let students create cache tables extremelly easy so they can learn more about the hardware and spend less time doing this stuff by hand.
### Author: @notZombieFood 

## How to
First, be sure you have installed pip and run this command.
```shell
pip install cache_tables
```
Load the libray into python
```python
import cache_tables
cache_tables.demo() #this will run some functions to demonstrate the functionality
```
## Code example, this should be easy to understand
```python
addresses = [3,180,43,2,191,88,190,14,181,44,186,253]
print ("Example 1 \nDirect Associative, with 8 blocks of 1 word \n")
cache_tables.directAssociative(addresses,8,1)
print ("Example 2 \nDirect Associative, with 4 blocks of 2 word\n")
cache_tables.directAssociative(addresses,4,2)
print ("Example 3 \nDirect Associative, with 2 blocks of 4 word\n")
cache_tables.directAssociative(addresses,2,4)
print ("Example 4 \nFull Associative Random, with 4 word\n")
cache_tables.fullAssociative(addresses,4,"RANDOM")
print ("Example 4 \nFull Associative FIFO, with 4 word\n")
cache_tables.fullAssociative(addresses,4,"FIFO")
print ("Example 4 \nFull Associative MRU, with 8 word\n")
cache_tables.fullAssociative(addresses,4,"MRU")
print ("Example 4 \nFull Associative LRU, with 8 word\n")
cache_tables.fullAssociative(addresses,4,"LRU")
```
## Help, this will give you further info
```python
help(cache_tables.fullAssociative)
```

## Will I implement partial associative?
Yes, sometime. But I can also receive some help if any of you wants to!



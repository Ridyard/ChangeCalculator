
'''using python generator objects - generator functions are a special kind of function that 
    return a lazy iterator. These are objects that you can loop over like a list. However, 
    unlike lists, lazy iterators do not store their contents in memory.'''

# simple script to make change from £1 - list all of the unique ways that different coin combinations can total a given amount

coins = [1, 2, 5, 10, 20, 50] # the coins that can make up £1
amount = 100 # signify £1 as 100p


# function will recursively try different combinations of coins & use generators to yeild results
# amount = the remaining amount of money to make change for; 
# coins = list of coins available; 
# hand = a list of coins being considered (ie a combination of coins)
def make_change(amount, coins, hand=None):
    hand = [] if hand == None else hand # initialize hand if it is not passed
    if amount == 0:
        yield hand
    for coin in coins:
        # ensures we don't give too much change & combinations are unique
        if coin > amount or (len(hand) >0 and hand[-1] < coin):
            continue
        
        # function calls itselfwith the remaining amount & the current combination of coins (hand + coin)
        # this call tries to find more coins to ake up the remaining amount
        for result in make_change(amount - coin, coins=coins, hand=hand + [coin]):
            yield result

# this will loop through the results of the make_change() generator
# as it is a generator, it doesn't compute all possible combinations at once, but yeilds one combination at a time - making it memory efficient
for way in make_change(amount, coins):
    print(way)



''' 
- Yield: The yield statement is what turns a function into a generator. It provides the value to the caller and "pauses" the function’s state until the next value is requested.
- Lazy evaluation: Generators compute values on the fly, which helps with memory efficiency.
- State retention: Unlike normal functions, generators maintain their state between calls, meaning the local variables and where it left off are remembered.
- StopIteration exception: A generator raises this when there are no more values to yield.
'''
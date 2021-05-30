import math
import unittest
import random

# functions for wallis pi construction

def wallis(nIter):
	prod=1;
	for i in range(1,nIter+1):
		exp=(4*i*i)/((4*i*i)-1)
		prod*=exp;

	prod*=2
	return prod


# function to calculate distance from origin
# check if its <=(0.5)(inside circle)
def distanceChk(x,y):

	d=((x-0.5)**2+(y-0.5)**2)**0.5
	if(d<=0.5):
		return True
	else:
		return False

# function to calculate pi using monte carlo
def monte_carlo(nThrows):

	countCircle=0
	countSquare=0
	for _ in range(nThrows):
		x=random.random()
		y=random.random()

		if(distanceChk(x,y)):
			countCircle+=1
		
		countSquare+=1

	piVal=4*(countCircle/countSquare)
	return piVal


class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()



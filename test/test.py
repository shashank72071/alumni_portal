import unittest

from gluon.globals import Request

execfile("applications/alumni_networks/controllers/apis.py", globals())


class TestAlumniNetworks(unittest.TestCase):
    def setUp(self):
        pass

    def testgetAlumni(self):
        # Set variables for the test function
        
        resp = getAlumni()
        self.assertEquals(3, len(resp))

    def testgetEvents(self):
        # Set variables for the test function
        
        resp = getEvents()
        self.assertEquals(1, len(resp))
    def testgetJobs(self):
        # Set variables for the test function
        resp = getJobs()
        self.assertEquals(2, len(resp))
    def testgetERequests(self):
        # Set variables for the test function
        
        resp = getERequests()
        self.assertEquals(1, len(resp))

    def testSearch(self):
        # Set variables for the test function
        
        resp = search("sunil","name")
        self.assertEquals(2, len(resp))
    def testgetApplierListForEvent(self):
        # Set variables for the test function
        
        resp = getApplierListForEvent("felicity")
        self.assertEquals(1, len(resp))
    def testgetApplierListForJob(self):
        # Set variables for the test function
        
        resp = getApplierListForJob("samsung")
        self.assertEquals(1, len(resp))
        
        

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAlumniNetworks))
unittest.TextTestRunner(verbosity=2).run(suite)

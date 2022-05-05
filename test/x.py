class TestCase:
  def __init__(self, name):
    pass

  def setUp(self):
    pass

  def run(self):
    method= getattr(self, self.name)
    method()

class WasRun(TestCase):
  def setUp(self):
    self.wasRun= None
    self.wasRun= 1

  def __init__(self, name):
    TestCase.__init__(self, name)

  

class TestCaseTest(TestCase):
  def testSetUp(self):
    test= WasRun("testMethod")
    test.run()
    assert(test.wasRun)

TestCaseTest("setUp").run()

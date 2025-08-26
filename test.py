from pyscript import document, display

@when("click", "#testbutton")
def testfunction():
  display("Test output")

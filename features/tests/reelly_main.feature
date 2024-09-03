Feature: Test for filter functionality


Scenario: User can filter by sale status Last Units
  Given Open reelly main page
  And Input email {kesha0801@gmail.com}
  When Click on “off plan” at the left side menu
  Then Verify the right page opens
  When Click on Sales status
  And Filter by sale status of “On Sale”
  Then Verify each product contains the "On Sale" tag




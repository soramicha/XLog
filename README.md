# XLog: Functional Expense Tracker by Sophia Chang

#### My project XLog (short for Expense Logger), is a functional expense tracker, where users can record the date, money, category, location, and memo for the day of their expense. Users can then keep track of those expenses with convenient bar charts and data tables.

### Video Link: https://youtu.be/m6YWHuTUWfU

### Functionalities

#### There are four main pages in XLog. The first one is the Record page. Users are required to input the date and amount of money for the day of their expense, as well as the category their expense would go in. There are a total of nine options users can pick for their category: Utility, Food, Gas, Mortgage/Rent, Transportation, Subscriptions, Healthcare, Personal Expenses, and Other. The last two inputs are optional, which are the Location and Memo fields. The location field is here to help the user know where they had spent that money, such as a supermarket or at a gas station. The memo field is a description field, where the user can add more information such as "Bought banana, strawberries, and kiwis" or "Purchased 5 gallons of gas". The convenient functionality in this page is that there is an "Add New Section" button, which the user can input more than one record of the same day, so they don't need to repeatedly enter the same date if they did multiple shoppings in one day. Once the user submits the records with the "Create" button, the records will be saved.

#### The second page is the Monthly Summary. There will be a data table which summarizes all of the expenses used in a particular month. The data table is grouped by category, and shows the sum of all expenses per category. At the bottom, there is a grand total which shows the total amount of money the user has spent that month, which is marked in bold. Users can also pick the specific months they want to see with month and year choice inputs. Below the table, there are individual records that are created for that month. Users can edit and delete any individual record, and doing so will automatically update the data table as well.

#### The third page is the Yearly Summary. It simply sums up all expenses for the whole year. Everything is organized by month and category. The Total Expenses column f the table sums up all expenses for every month, while the Grand Total row shows the sum of expenses per category, and the total amount of money spent for the WHOLE year. Again, the user has the flexibility to control which year they want to see.

#### The fourth and final page is the Home/XLog Page. There is a bar chart which functions just like a Yearly Summary table would do, with the difference being the fact that users can visually see their total expenses for the year. There is a legend that shows all nine categories. Clicking any category in the legend will show or hide the data for that specific category. This way, users can conveniently and easily compare specific categories between months. And just like the Monthly and Yearly Summary pages, the Home page allows users to pick whichever year they want to see for the bar chart.

#### An extra functionality added to this project is the dark/light mode function. Clicking on the dark/light mode will change the whole page's color mode, with a pink theme representing light mode and a dark blue theme representing dark mode.

### Challenges

#### The complexity of this project mainly lies within the implementation of the charts. I've never used Chart.js until now, but learning how to properly make my own chart took a while for me, especially when I have to update the chart every time a user flips on the dark/light mode or whenever a user changes the year of the bar graph. The dark and light mode function also took some time as well, because I have to make sure every single page will change colors accordingly whenever the dark/light mode button is clicked on, and keep that mode for every other page that gets clicked on until it switches again.

## How to Run the Application

#### Type in python3 manage.py runserver to run the application. There are no additional Python packages necessary to run this application.

## Why I Chose to Make an Expense Tracker

#### I'm currently a college student and there are times where I go out with my friends to eat, etc. I realize I don't keep track of the amount of money I spend and I want to prioritize spending money efficiently, so with that being said, I decided to make my own expense tracker. It will benefit me and I can learn to save money with this.

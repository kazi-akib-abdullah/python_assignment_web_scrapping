# python_assignment_web_scrapping

### Tools
 - Python
 - Html-parser
 - re
 - urllib
 - mysql.connector
 - Xampp
 - ssl

### Required Instruction

- Run xampp on localhost
- Import .sql file to database[XAMPP];
- Run the .py file to execute

### Database Screenshot

![](https://github.com/kazi-akib-abdullah/python_assignment_web_scrapping/blob/main/Screenshot%20from%202021-12-08%2013-52-41.png)
### Create Table Cmd
``` mycursor = mydb.cursor()
create_table='''CREATE TABLE Villa(
                    Name varchar(250) NOT NULL,
                    Sleeps varchar(30),
                    Bedroom varchar(30),
                    Bathroom varchar(30),
                    Price varchar(10),
                    Image1 varchar(500),
                    Image2 varchar(500),
                    Image3 varchar(500),
                    PRIMARY KEY (Name))
                    '''
mycursor.execute(create_table)  ```


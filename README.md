# SecurePass – Smart Password Strength Checker
YouTube link: [https://youtu.be/raqvOrapmQc](https://youtu.be/raqvOrapmQc)
Github link: [https://github.com/weekndbaba/securepass-password-checker](https://github.com/weekndbaba/securepass-password-checker)
SecurePass is a password strength checker web application built using the Flask web framework, designed to help users assess the strength of their passwords in real-time. This project is intended to help users understand the strength of their passwords and ensure they use strong and secure passwords when creating accounts or managing their digital life. The app evaluates password strength based on length, complexity (uppercase, lowercase, numbers, special characters), and provides visual feedback on its strength through a dynamic progress bar. Additionally, users can track their past password checks through a history dashboard, which helps them monitor their password choices over time.

This application has been developed as part of my CS50 Final Project, demonstrating my proficiency in Python, web development, and database integration.

## Project Overview
Password security is one of the cornerstones of online safety, and ensuring users choose strong passwords is crucial. SecurePass provides an intuitive, user-friendly interface that categorizes passwords into three strength levels: Weak, Medium, and Strong. The strength is calculated based on several factors, such as:

Length of the password

Presence of uppercase and lowercase letters 

Inclusion of numbers

Use of special characters

The application displays the password strength in the form of a progress bar that fills based on the strength score, alongside a text-based description of the password's strength. It also offers useful tips to improve weak passwords, like adding more characters or including special symbols.

One of the major features of SecurePass is the password history dashboard. This feature allows users to view previously tested passwords, with a record of the password’s length, strength rating, and the timestamp of when it was checked. This feature gives users an overview of their password habits and can serve as a reminder to improve their security practices over time.

## File Descriptions
1. app.py
This is the main file of the application, and it serves as the Flask application that runs the server. It contains the routes for the homepage and the dashboard.

/ (index route) handles the logic for password strength evaluation. This route receives the password input from the user, calculates the strength using the calculate_strength function, and renders the result.

/dashboard displays the password history stored in the SQLite database.

The app.py file also initializes the SQLite database to store user data about password history and strength. The password history is stored in a simple table with fields like the password's length, strength, and timestamp of when the password was evaluated.

2. templates/
This folder contains the HTML files responsible for rendering the user interface.

index.html: The main page where users input their passwords for strength evaluation. This page uses a Bootstrap 5 form to capture the user’s password and dynamically displays the password strength as the user types. It also shows suggestions for making weak passwords stronger.

dashboard.html: The dashboard page displays a list of previously checked passwords along with their strength, length, and timestamp. The data is pulled from the SQLite database and presented in a simple, readable table format.

Both HTML files use Bootstrap 5 for responsive design, ensuring that the app looks good on any device. They also utilize custom CSS styles for additional customization and to match the design choices made for the project.

3. static/style.css
The CSS file contains custom styles that enhance the user interface. While Bootstrap provides a basic layout, the style.css file defines specific styles for the password strength meter, table layouts on the dashboard, and general formatting for the app. It helps the app stand out with unique visual elements, making the experience more engaging for the user.

4. passwords.db
This is the SQLite database used to persist password history data. The database contains a single table, passwords, which stores records of the evaluated passwords. The columns in the table are:

id (Primary key)

password_length (Length of the password)

password_strength (Strength category: Weak, Medium, or Strong)

timestamp (Date and time when the password was checked)

This database ensures that users' password history is stored and can be retrieved later for reference.


## Design Choices and Considerations

While building SecurePass, several design decisions were made to ensure that the app is both functional and user-friendly:

Real-Time Feedback: The decision to provide real-time feedback as users type their passwords ensures an interactive and dynamic user experience. It allows users to see how strong their passwords are immediately, giving them the opportunity to adjust and improve their passwords as they go.

Strength Meter: The progress bar visually indicates the password’s strength, making it easier for users to understand their password’s security at a glance. The color-coded feedback (red for weak, yellow for medium, and green for strong) is intuitive and gives users immediate insight.

Password History: Storing password history gives users the ability to monitor their password security practices over time. The dashboard also allows them to compare their past password strengths and make improvements.

SQLite for Persistent Storage: SQLite was chosen due to its simplicity and the fact that it is an integrated database that doesn’t require a separate server. This allows the app to function as a self-contained, local application without the overhead of managing an external database.

Bootstrap for UI: Bootstrap 5 was used for responsiveness and to quickly develop a professional-looking UI without building all the components from scratch. It ensures the app works seamlessly on all devices, including mobile phones, tablets, and desktops.

## Future Improvements
User Authentication: Adding user authentication would allow users to have personalized dashboards, where they can track password history across multiple devices.

Password Generation: A password generation tool could be added to help users create strong, random passwords.

Security Features: Integration with HaveIBeenPwned API to check if a password has been compromised in any known data breaches would further enhance the security features of the app.

## Sources

[Flask docs](https://flask.palletsprojects.com/en/stable/)
[Python docs](https://docs.python.org/3/)
[Bootstrap docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)


## Conclusion
This project demonstrates my understanding of web development, security concepts, and database integration. By building SecurePass, I was able to apply my skills in Flask, HTML/CSS, and SQLite, and I learned how to build a functional and interactive web application. The app provides a simple yet powerful tool for users to ensure they are using strong passwords, an essential practice in maintaining online security.

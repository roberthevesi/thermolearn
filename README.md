**Thermolearn**

**Description:**

This repository contains the code for Thermolearn.

**Structure:**

The project is organized into the following directories:

-   `thermolearn-backend`: Includes the server implemented in Java using Spring Boot.
-   `thermolearn-frontend`: Contains the code for the client application, built with React Native using Expo.
-   `thermolearn-device`: Houses the main processing script written in Python and C++.
-   `thermolearn-model`: Includes the Machine Learning model.

**Prerequisites:**

Before running the project, make sure you have the following software installed on your system:

-   Node.js and npm: For the client application.
-   Python 3.11.2: For the main processing script.
-   Java 19: For the server.

**Running the Application:**

1. Clone this repository:

    ```bash
    git clone https://github.com/roberthevesi/thermolearn.git --recurse-submodules
    ```

2. Navigate to the project directory:

    ```bash
    cd thermolearn
    ```

3. Install & Run the Application:

    - **Client Application (thermolearn-frontend):**

        ```bash
        cd thermolearn-frontend
        npm install
        npx expo start -c --offline
        ```

    - **Main Processing Unit (thermolearn-device):**

        Make sure you have Python installed:

        ```bash
        cd thermolearn-device/Pi
        python script.py
        ```

    - **Server (thermolearn-backend):**

        Make sure you have Java installed. The server code is packaged as a JAR file, you don't need to install additional dependencies:

        ```bash
        cd thermolearn-backend
        java -jar api-0.0.1-SNAPSHOT.jar
        ```

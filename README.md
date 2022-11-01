<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://drive.google.com/uc?export=view&id=1twqwlJ7k7Xu5C9JO9uwUjVlc5OJO109x" alt="Logo" width="200" >
  </a>

  <h3 align="center"><b>PADDLE RANKING</b></h3>

  <p align="center">
   Serverless Web scraping automatic pipeline for paddle ranking.
    <br />
    <br />
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About the Project">About the Project</a></li>
    <li><a href="#built with">Built With</a></li>
    <li><a href="#api">API</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#pre-requisites">Pre-requisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#author">Author</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<br>

<!-- ABOUT THE PROJECT -->
# 1. About the Project 📢


 <img src="https://drive.google.com/uc?export=view&id=17ELf6JuMo1UeXZ2_fL_9pEMmUkbi3mwg" alt="Diagram icon">

</br>

The project cosist of a web scraping serverless system that allows to get the ranking of the paddle players in the world. The system is composed by web scraping functions pipeline that is triggered by a cron job. The pipeline ends into a NoSQL database and expose data by an API.

<p align="right">(<a href="#top">back to top</a>)</p>



# 2. Built With 🛠️

[Serverless Framework](https://www.serverless.com/): Framework to implement IaaC with cloud providers.

[AWS Services](https://aws.amazon.com/es/):
* [Lambda](https://aws.amazon.com/es/lambda/): Serverless logic functions
* [SNS](https://aws.amazon.com/es/sns/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc): Service notification system to comunicate services
* [DynamoDB](https://aws.amazon.com/es/dynamodb/): NoSQL database
* [API Gateway](https://aws.amazon.com/es/api-gateway/): API Rest management
* [CloudWatch event](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html): Schedule the system trigger.
* [X-Ray](https://aws.amazon.com/es/xray/): Service to trace and monitor the system services.


_GOOD PRACTICES APPLIED_

* **FAN-IN** and **FAN-OUT** patterns apply for lambda parallelization with SNS

* SNS to apply first **SOLID principle (SRP)**

* TLL created to delete database data before new paddle ranking data is web screaped.

* Secondary Index created in the player table to reduce DynamoDB cost for get services

* Services tracing
 
And more...

<p align="right">(<a href="#top">back to top</a>)</p>


# 3. API 🚀

The API Rest is full docummented and you can use it for your projects [Rapid API](https://rapidapi.com/search/paddle)

# 4. Getting Started 🛠️  

This is an example of how you may give instructions on setting up your project and deploy to AWS cloud. This is an example of how to list things you need to use the software and how to install them.
## Pre-requisites
* npm
  ```sh
  npm install npm@latest -g
  ```
* serverless
  ```sh
  npm install serverless@latest -g
  ```

## Installation  

1. Clone the repo
   ```sh
   git clone https://github.com/JoseRamonMartinez/padel-aws.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```
3. Create a `config.yml`
   ```yml
    playersTableName: <CustomName>
    playersSeeder: [./seeds/<CustomName.json>]
    scrapingTopicName: <CustomName>
    postPlayerTopicName: <CustomName>
    apiUrls:
      players: <CustomName>
    accountIdNumber: <AWS_ACCOUNT_ID_NUMBER>
    stage: <Stage>
    region: <AWS-REGION>
   ```

2. Deploy to AWS
   ```sh
   sls deploy --<aws-profile>
   ```
</br>

# 5. Author ✒️

<h3>José Ramón Martínez Riveiro &nbsp;
<a href="https://www.linkedin.com/in/joseramonmartinezriveiro/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://joseramonmartinez.github.io/"><img src="https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white"></a>
</img>
</h3>

</br>
</br>

# 6. License 📄
`Copyright` © 2022, José Ramón Martínez Riveiro. 


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->

[aws-shield]:  	https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white?style=for-the-badge

[aws-url]: https://aws.amazon.com/

[license-shield]: https://img.shields.io/badge/LICENSE-COPYRIGHT-yellow?style=for-the-badge
[license-url]: https://img.shields.io/badge/LICENSE-COPYRIGHT-yellow?style=for-the-badge

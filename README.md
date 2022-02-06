<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![CD][deploy-shield]][deploy-url]
[![Stargazers][stars-shield]][stars-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://drive.google.com/uc?export=view&id=1twqwlJ7k7Xu5C9JO9uwUjVlc5OJO109x" alt="Logo" width="200" >
  </a>

  <h3 align="center">PADDLE RANKING</h3>

  <p align="center">
    Web scraping for paddle ranking and API Rest to consume services
    <br />
    <br />
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#api-usage">API Usage</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#author">Author</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<br>

<!-- ABOUT THE PROJECT -->
# 1. About The Project 📢


 <img src="https://drive.google.com/uc?export=view&id=17ELf6JuMo1UeXZ2_fL_9pEMmUkbi3mwg" alt="Diagram icon">

</br>

The project consist into a  web scraping system that saves updated paddle data from wpt in our database. This system is scheduled to trigger automatically. Furthermore, the system provide an API Rest to consume services.

<p align="right">(<a href="#top">back to top</a>)</p>



# 2. Built With 🛠️

[Serverless Framework](https://www.serverless.com/): Framework to implement IaaC with cloud providers.

[AWS Services](https://aws.amazon.com/es/):

* [Lambda](https://aws.amazon.com/es/lambda/): Serverless logic functions
* [SNS](https://aws.amazon.com/es/sns/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc): Service notification system to comunicate services
* [DynamoDB](https://aws.amazon.com/es/dynamodb/): NoSQL database
* [API Gateway](https://aws.amazon.com/es/api-gateway/): API Rest management
* [CloudWatch event](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html): Schedule the system trigger. 


_GOOD PRACTICES APPLIED_

* **FAN-IN** and **FAN-OUT** patterns apply for lambda parallelization with SNS

* SNS to apply first **SOLID principle (SRP)**

* TLL created to delete database data before new paddle ranking data is web screaped.

* Secondary Index created in the player table to reduce DynamoDB cost for get services
 
And more...

<p align="right">(<a href="#top">back to top</a>)</p>


# 3. API 🚀

The API Rest is full docummented and you can use it for your project [Rapid API](https://rapidapi.com/search/paddle)

# 4. Getting Started 🔧  

This is an example of how you may give instructions on setting up your project and deploy to AWS cloud.

## 4.1 Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
* serverless
  ```sh
  npm install serverless@latest -g
  ```

## 4.2 Installation 🛠️ 

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
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
      players: CustomName
      scraping: CustomName
    accountIdNumber: <AWS_ACCOUNT_ID_NUMBER>
   ```

2. Deploy to AWS
   ```sh
   sls deploy --<profile>
   ```


<!-- CONTACT -->
# 5. Author ✒️

José Ramón Martínez Riveiro - [Linkdedin](https://www.linkedin.com/in/joseramonmartinezriveiro/) - josera.martinez@hotmail.com

[Online Portfolio](https://joseramonmartinez.github.io/)
</br>
<br>
<!-- LICENSE -->
# 6. License 📄
`Copyright` © 2017, José Ramón Martínez Riveiro. 


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[deploy-shield]: https://github.com/JoseRamonMartinez/api-padel/action/workflows/cd-serverless.yml/badge.svg
[deploy-url]: https://github.com/JoseRamonMartinez/api-padel/actions/workflows/cd-serverless.yml
[stars-shield]: https://img.shields.io/github/stars/JoseRamonMartinez/api-padel.svg?style=for-the-badge
[stars-url]: https://github.com/JoseRamonMartinez/api-padel/stargazers
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/joseramonmartinez
[product-screenshot]: images/screenshot.png
<img src="https://i.ibb.co/TMh0Yb7/Onspot.png" width="206" height="206">

# Onspot - An AI Powered Secured Utility Complaint System Cloud Computing

## Onspot Core Backend (Object Detection + Flask API)

### Introduction and Motivation

- A major problem being faced by municipalities around the world is maintaining the condition of roads be it summer, the monsoons (when it is at its worst) or any weather condition as a matter of fact. And although it’s the responsibility of the authorities to make sure the roads are free of damage, at times they overlook the problem, and most times don’t even know that the problem exists. According to indiatoday, the number of deaths over the past 3 years stands at 9300 and with over 25000 injuries. 
 
- Maintaining the road condition is a challenge with constant weather changes, wear and tear, low budgets for the municipalities. Also, not to forget keeping people informed is a task. So, this is an application aimed at solving the challenges mentioned. A reporting system, where the citizen can capture the scene of an area, which will be fed to a machine learning model that will geocode, validate and track down potholes in the scene. This would be achieved by training for object tracking on multiple images and developed using convolutional neural networks. Users can see the damage on the roads using a mobile application or through their browsers. A dynamic report is also generated for the closest authority of concern which they can view and update to create and manage work orders using their own jurisdiction-based web/mobile app-based dashboard.

### Motivation

- Keeping the roads in good condition along with tracking damages is a challenge with constant changes in weather, low budgets for the municipalities. Not to forget keeping the people informed is a task. This project was aimed at solving the challenges mentioned above and was aimed at solving the challenges mentioned above by creating an interactive environment between the municipality and any person who identifies a pothole in a dynamic environment.

- In articles covered by Guardian News & Media potholes took a deadly toll in 2017, claiming almost 10 lives daily. IndiaTimes stated that "Bereaved Father Mr. Dadarao" filled 600 Potholes in Mumbai in memory of the son he lost in a road accident! Inshorts reported, potholes killed more people than terrorists reporting 14,926 deaths in road accidents.

### Project URLs and Overview

#### Application demo

- Link to our Citizen's App Demo: https://onspot.click/onspot/
- Link to Authority App Demo: https://onspot.click/onspot.authority/

#### Presentation
- Link to Google slides Presentation: [ONPSOT PRESENTATION](https://docs.google.com/presentation/d/11WXTHG384vmLA67QShnrbcqOba3xjXWjqkf6utVPv64/edit#slide=id.g111b81d1d86_3_5)

#### Citizen App Repository

Link to Citizen App's Repository: https://github.com/kuluruvineeth/onspot.backend/edit/main/README.md

#### Authority App Repository 
- Link to Authority App's Repository: https://github.com/kuluruvineeth/onspot.authority

### Process Description

#### The backend comprises of the following three main sections
- The first being the object detection model built using Darkflow. 
- The second being the database for the application. 
- The third being the Flask API for data exchange between the model built, the database and the frontend.

#### 1. Object Detection Model

- The focus of the backend application was to create a rest api to automate the process of pothole validation with media files, from the start, a cloud server was used for implementation. A [EC2 Amazon Web Services Instance](https://aws.amazon.com/ec2/instance-types/) was used for this purpose.

- AWS EC2 C5 Instance (model: c5.xlarge) after choosing Ubuntu 20 which features the Intel Xeon E5-2666 v3 (code name Haswell) processor and offers a set of 1vCPU with 7.5 GiB of memory was chosen for training the object detection model. Please refer the deployment section to learn more about setting this up. 

- For hosting the application using apache2 webserver and also for dumping the data into the database, a t2.small instance was used featuring the Intel Xenon processors. 

- The model is trained on top of [Darkflow](https://github.com/thtrieu/darkflow) and built on top of pretrained weights which were obtained from [Darknet](https://pjreddie.com/darknet/).

- For crawling images relevant to our label ‘pothole’, images were crawled using the open source google image search package, along with the serpapi image search tool.

- Along with this, freely available pothole video feeds to create the dataset were also used. For a near to decent detection result, we should look to collect almost 500+ images. The dataset has been provided with the repository.

- For video files, we can upload it to our server using an sftp client such as Filezilla or by directly using ssh on the terminal of our local machine. The next step was to write a script to slice this uploaded video into images by dividing the entire video into frames and storing them into a custom frames folder. Python’s OpenCV (cv2 package and Video Capture Module) to divide the feed into frames.

- Use the following commands to install the dependency packages
  ```pip install pillow
       pip install lxml
       pip install jupyter
       pip install matplotlib
       pip install protobuf
   ```

- After cloning the DarkFlow repository, we need to prepare the input files for DarkFlow we need to consider two things. 
 * Firstly, we need an RGB image which is encoded as jpeg or png.    
 * Secondly, we need a list of bounding boxes (xmin, ymin, xmax, ymax) for the image and the class of the object in the bounding box.

- Our class, in this case, is ‘pothole’. We then need to label our images with a tool like LabelImg to identify areas of interest with bounding boxes(For preparing our training dataset)

- LabelImg is a graphical image annotation tool that is written in Python and uses Qt for the graphical interface. It supports Python 2 and 3. The annotations are saved as XML files in the Pascal VOC format We can split the data to train and test sets before running the training command. For more details please take a look at the [report](Report link to be kept)

- Now the datasets needed to be fed to the darkflow package in the required format are available.

- We need to first configure Darkflow by modifying the configuration file and labels.txt file.

- Then we need to make a copy from cfg/tiny-yolo-voc.cfg and create a cfg/tiny-yolo-voc-1c.cfg file with the same content. Change the line 114 to filters=30 [num * (classes + 5)] and set classes=1 as we have only one class ‘pothole’.

- In the label.txt file remove all the labels and just keep the pothole label.

- Once done, refer to the following link for better clarity. [Preparing dataset and training it with Darkflow](https://medium.com/coinmonks/detecting-custom-objects-in-images-video-using-yolo-with-darkflow-1ff119fa002f), and start training with the dataset.

- Using the test sets the model can be verified to check the accuracy of our newly trained object tracking model. This can now also be applied to various snippets of video to highlight the potential of object detection on potholes. Refer to the link mentioned in the above step for the testing command. It also contains options to restart training from a previous checkpoint, etc.

- Now we can proceed to saving the built graph as a protobuf file. Read this link on [Darkflow](https://github.com/thtrieu/darkflow#save-the-built-graph-to-a-protobuf-file-pb) to understand this better.

```
flow --pbLoad built_graph/yolo.pb --metaLoad built_graph/yolo.meta --imgdir sample_img/
```

- The dataset, the annotation files, the built model have all been provided with the repository for reference. You can follow the steps mentioned above only if you wish to have a fresh start to training and testing the model(Would recommend this).

#### 2. Database

- The database is comprised of 4 main entities. (Authority, Public User, Reports, Comments).

- Please refer the database schema to know more about the attributes associated with each entity.

- The authority is someone who has the authorization to manage reports in their zone. A zone is specified as a 5000 mts radius. Also please note that an Authority does not require to be registered in the application(This is taken care by the system administrators only for obvious reasons)

- A public user is someone who can create a report using the citizen app.

- A report is basically details of a submission that has been validated using the object detection model.

- Comments are basically communication exchange between an authority and a user on a report.

- A service layer file in python has been created with different methods which are used by the api to communicate with the database for performing CRUD operations.

#### Schema Diagram

<img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/MySQL_Database/onspot_db_schema.png" alt="Schema Diagram">
 
#### 3. Flask API 
 * The Flask API has been built for data exchange between the front end applications, the object detection model and the database. 
 
 * For understanding the front end side of things please refer the important urls section of this read me file. 
 
 * A app controller script has been created to communicate with the service layers (mysql, mail service and parent(object detection))
 
 * The following endpoints have been created for the APIs and each of them have been tested using POSTMAN.
 
 | End Point                         | Description                                                        | Method | Required Params (Keys)                                                 | Application        |
| --------------------------------- | ------------------------------------------------------------------ | ------ | ---------------------------------------------------------------------- | ------------------ |
| /api/profile/authority/update     | For updating a authority's profile details                         | POST   | authorityId, emailId, name, photoURL                                   | Authority          |
| /api/authority/check              | For validating auhtority credentials                               | POST   | emailId                                                                | Authority          |
| /api/authority/reports/geonear    | For querying reports in an authority's zone                        | POST   | authorityId                                                            | Authority          |
| /api/authority/update/report      | For updating a report's status (for authority)                     | POST   | severity, status, caseId                                               | Authority          |
| /api/profile/authority/data       | For retreiving a authority's profile details, location and address | POST   | authorityId                                                            | Authority          |
| /api/authority/update/user/status | For changing the status of a user (blocked / allowed)              | POST   | userId, status                                                         | Authority          |
| /api/authority/send/email         | For notifying a user via email                                     | POST   | emailId, message, subject                                              | Authority          |
| /api/reports/all                  | For retrieving all users reports                                   | POST   | (N/A)                                                                  | Citizen, Authority |
| /api/reports                      | For retrieveing a particular user's reports                        | POST   | userId                                                                 | Citizen, Authority |
| /api/submit/report/comment        | For submitting a comment on a report                               | POST   | userType, commentText, caseId                                          | Citizen, Authority |
| /api/reports/comments             | For retrieving all comments on a report                            | POST   | caseId                                                                 | Citizen, Authority |
| /api/submit/report                | For submitting a new report                                        | POST   | description, location, latitude, longitude, imageURL, severity, userId | Citizen            |
| /api/upload                       | For uploading files to the server                                  | POST   | bytes (file data)                                                      | Citizen            |
| /api/detect/single                | For detecting whether an image has a pothole. (Object Detection)   | POST   | image_url                                                              | Citizen            |
| /api/profile/update               | For updating a user's basic profile details                        | POST   | userId, emailId, name, photoURL                                        | Citizen            |
| /api/user/validate                | For validating a user's status (allowed / blocked)                 | POST   | emailId                                                                | Citizen            |

#### System Level Design

- To be kept

### Key Features
| Feature Name | App Usage |
| --- | --- |
| Darkflow, Darknet Incorporation | Backend |
| Pothole Detection / Validation (Images, Video) | Citizen |
| Protobuf Compilation (Model) | Backend |
| Image Annotations | Backend |
| Rename and Rearrange Files (Script) | Backend |
| Image Crawler on top of PyImage Search | Backend |
| Video File Slicing (Script) | Backend |
| Output File Storage | Backend | 
| Route 53 (Hosted Zone) on Amazon Web Services (AWS) | Backend | 
| SSL Configuration | Backend |
| Security Groups (AWS) | Backend |
| Media Uploads | Citizen |
| CRUD Operations Authorities Entity | Authority, Citizen |
| CRUD Operations Public Users Entity | Authority, Citizen |
| CRUD Operations Comments Entity | Authority, Citizen |
| CRUD Operations Reports Entity | Authority, Citizen |
| Email Service | Authority |
| Allow / Block User Status | Authority |
| App User Authorization Check | Authority, Citizen |
| Geo Near Reports Querying | Authority |
| Flask API Controller | Authority, Citizen |

### Tools, Libraries and Languages Used

- The Backend Application has been built with Python at its Core.
- The REST API has been built with Flask.
- The Object Detection Model has been built using DarkFlow on top of Darknet.
- The Final Model is a Protobuf Compilation (Minified).
- Mysql has been used for Database needs.
- Package smptlib has been used for Sending Emails.
- Package flask_cors has been used to manage Cross Origin Requests.
- Package mysql is used to interact between Python and MySql.
- Package cv2 is used to create Bounding Boxes at Runtime.
- The Parent Service which Communicates with the Deep Learning Model uses the TensorFlow Model created.
- Amazon Web Services has been used for Deployment Purposes.
- Certbot has been used for HTTPS Configuration
- Freenom has been used for Domain needs.
- Apache is used for Server needs.
- FileZilla and GitBash are used for SFTP and SSH needs.
- Chrome Dev Tools and Postman were used for API Manual Testing.

### Technology Stack (For both Frontend and Backend)

<img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/architectural_tiers/architectural_tiers.png"/>

### Instructions to Set-Up and Deploy the Backend Application

#### Amazon Web Instance Set-Up and Configuration

- The authority's application has been hosted through Amazon Web Services. To set up the application on a EC2 Instance and a Route 53 Hosted Zone for your choice of Domain Name from a site like Freenom for free refer the following screenshots.

- Login to the Amazon AWS Console. Once registered and logged in successfully click on Launch EC2 Instance. Follow the steps in the screenshots.

<img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/aws/instanceAMI.png" alt="aws">
<img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/aws/instanceType.png" alt="aws">
<img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/aws/InstanceConfig.png" alt="aws">
<img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/aws/InstanceStorage.png" alt="aws">
<img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/aws/InboundRules.png" alt="aws">

- Your console should now look similar to this after a successful launch.

<img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/aws/InstanceState.png" alt="aws">

For connecting your domain, search for Route 53 in the app bar and create a hosted zone. Create a new hosted zone and then record sets for connecting your domain. Use this name servers in your domain's settings to form a connection both ways.

<img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/aws/route53.png" alt="aws">

#### Darkflow Set-Up

- Follow the discussion in the process description above. In addition to that refer the README.md file for the darkflow repository. View the links mentioned in the process description and finally review the official documentaion on Darknet.
- Here are some important links. [Darknet](https://pjreddie.com/darknet/), [Darkflow](https://github.com/thtrieu/darkflow), [Training YOLO with DarkFlow](https://sites.google.com/view/tensorflow-example-java-api/complete-guide-to-train-yolo/train-yolo-with-darkflow)

#### MySQL Set-Up

- Please follow a setup guide like [this](https://linuxize.com/post/how-to-install-mysql-on-ubuntu-18-04/) to setup MySQL on to your instance.
- Import the .sql file provided in the repository to finish setting up mysql for the purpose of this application. After these steps use the below commands to start mysql to view the dumped data. By default the username and password are set to be root in the instance.
 ```
  mysql -u <username> -p <password>
  use database onspot;
  show tables;
  select * from <table_name from above output>
  ```
#### Flask Set-Up

- You can follow this guide to learn about setting up Flask. [Guide](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/)
- You will have to make changes in the utility file under the flask app's directory by changing the directory constants according to project structure.
- For running on https you will have to setup certbot and use your key files after setting up the ssl certificate in the app controller(Recommended). Or you can ignore that and run on http.
- We have also tested the respective endpoints mentioned above using POSTMAN. Feel free to refer them to get an idea on how to feed data to the backend(using JSON)

  * /api/authority/check:
    <img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/postmanAPI%20Testing/Authority/api-authority-check.png" alt="api">
    
  * /api/authority/reports/geonear
    <img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/postmanAPI%20Testing/Authority/api-authority-reports-geonear.png" alt="api">
  
  * /api/authority/send/email:
     <img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/postmanAPI%20Testing/Authority/api-authority-send-email.png" alt="api">
   
   * /api/authority/update/report:
     <img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/postmanAPI%20Testing/Authority/api-authority-update-report.png" alt="api">
     
   * /api/authority/update/user/status:
     <img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/postmanAPI%20Testing/Authority/api-authority-update-user-status.png" alt="api">
   
   * /api/profile/authority/data:
     <img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/postmanAPI%20Testing/Authority/api-profile-authority-data.png" alt="api">
     
   * /api/profile/authority/update:
     <img src="https://github.com/kuluruvineeth/onspot.backend/blob/main/screenshots/postmanAPI%20Testing/Authority/api-profile-authority-update.png" alt="api">

#### Apache Set-Up

- Follow this guide to learn more. [Apache Setup](https://ubuntu.com/tutorials/install-and-configure-apache#1-overview).

#### Certbot Set-Up

- Follow this guide to setup a ssl certificate for your ubuntu ec2 instance [Guide](https://www.webcreta.com/how-to-letsencrypt-ssl-certificate-install-on-aws-ec2-ubuntu-instance/)

#### Hurray! You've done it. Enjoy using the app and feel free to make contributions and raise pull requests. Run the app_controller python file to see your api running.

### Future Scope
* Severity based Direction Renderer.
* Adding Additional Parameters to the Frontend after Implemented in the Backend. (Pothole Dimensions) 
* Offline Capabilities for the camera component.
* Realtime Notifications in the application itself.
* Linking via Social Platforms like twitter, facebook, etc.
* News Feeds
* Interaction using a gamified approach to challenge peers using rewards.

### Note

In case if you wish to contribute to the project, feel free to do so. Please review the future work sections also and create pull requests for ideas and thoughts.

### Acknowledgements and References

* @reactjs - https://reactjs.org/
* @material-design-react - https://material-ui.com/
* @react-google-maps - https://www.npmjs.com/package/react-google-maps
* @google-maps-api - https://developers.google.com/maps/documentation/javascript/
* @google-oauth-gapi - https://developers.google.com/identity/protocols/oauth2
* @mui-treasury - https://mui-treasury.com/
* @axios - https://www.npmjs.com/package/axios
* @filepond - https://www.npmjs.com/package/filepond
* @dateformat - https://www.npmjs.com/package/dateformat
* @loadash - https://lodash.com/
* @create-react-app - https://reactjs.org/docs/create-a-new-react-app.html
* @gh-pages - https://www.npmjs.com/package/gh-pages
* @github - https://github.com
* @trello - https://trell.com
* @figma - https://figma.com
* @google-keep - https://keep.google.com
* @npmjs - https://www.npmjs.com
* @snap2html - https://www.rlvision.com/snap2html/about.php




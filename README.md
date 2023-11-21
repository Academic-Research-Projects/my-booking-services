# My Booking services
Team :
👨🏼‍🦱 Corentin BAUDET
👩🏻 Génesis LOIZAGA
👦🏻 Jean-Antoine MARO
🧔🏻 François UTZMANN

The aim of this school project is to work in a DevOps context, building a microservices web application on a clustered infrastructure. One of the major constraints has been the continuous deployment of our work.

## Context of the project
The client, a hotel chain, wants to set up a single reservation system for all hotels and all sales channels (telephone, reception, website, mobile application).

The role of the team is to set up a hotel booking API. The customer wants to be able to quickly benefit from a first batch of features. Rooms reservation, number of people per room booked, breakfast, cancellation of reservations, garage, wifi, etc.

### Tools and technologies
- Docker Swarm
- Ansible
- Gitlab & Gitlab CI
- Django Python

## The infrastructure


## The microservices architecture

![Pipeline CI_CD - Page 2](https://github.com/Academic-Research-Projects/my-booking-services/assets/61324708/228a52ab-d285-432e-b227-6749ca201af3)


## The web application
We have developed a Django - Python backend API. One of the requirements being to deliver an API in a microservices applications, we have decided to split the API in 4 services : Users API, Bookings API, Catalogue API and Pricing API. In this way, we also split our databases per object, for a better resilience of the services.

[to be continued]

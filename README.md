[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]





<!-- ABOUT THE PROJECT -->
## About The Project


### Built With

* [Morpheus]('https://morpheusdata.com/)
* [Python]('https://www.python.org/)





### Prerequisites

 - Integrate git repo into Morpheus
 - Create task to run main.py
 - Create scheduled job to run the task
 - Create monitoring checks (PushAPI)



<!-- USAGE EXAMPLES -->
## Usage
> Command Arguments must be used sequentially as documented below

Task Args:
1. `appliance_name` - This is hostname or IP only
2. `client_id` - Available options are:  `morph-api, morph-automation, morph-cli, morph-customer`
3. `access_token`: This is either a quoted string or a cypher entry variable (ex:`<%= cypher.read('secret/access_token') %>`)
4. `refresh_token`: This is either a quoted string or a cypher entry variable (ex:`<%= cypher.read('secret/refresh_token') %>`)
5. `critical_check_apikey`: This corresponds with the API key provided by the critical monitoring check upon creation.
6. `critical_check_apikey`: This corresponds with the API key provided by the warning monitoring check upon creation.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/boxedlunch-us/morpheus-api-key-rotation/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/boxedlunch-us/morpheus-api-key-rotation.svg?style=for-the-badge
[contributors-url]: https://github.com/boxedlunch-us/morpheus-api-key-rotation/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/boxedlunch-us/morpheus-api-key-rotation.svg?style=for-the-badge
[forks-url]: https://github.com/boxedlunch-us/morpheus-api-key-rotation/network/members
[stars-shield]: https://img.shields.io/github/stars/boxedlunch-us/morpheus-api-key-rotation.svg?style=for-the-badge
[stars-url]: https://github.com/boxedlunch-us/morpheus-api-key-rotation/stargazers
[issues-shield]: https://img.shields.io/github/issues/boxedlunch-us/morpheus-api-key-rotation.svg?style=for-the-badge
[issues-url]: https://github.com/boxedlunch-us/morpheus-api-key-rotation/issues
[license-shield]: https://img.shields.io/github/license/boxedlunch-us/morpheus-api-key-rotation.svg?style=for-the-badge
[license-url]: https://github.com/boxedlunch-us/morpheus-api-key-rotation/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/boxedlunch-us
# FYP - Harry Hawkins - A cloud-based solution to IIOT server monitoring
Final Year Project Repository
Supervisor: George Parisis

Proposal - A cloud-based solution to IIOT server monitoring
Introduction
As we become a more interconnected society, the use of Industrial Internet of Things (IIOT) devices is increasingly prevalent. They are commonly found in wind farms, electric vehicle charging stations, power stations, factories, as well as a whole array of industries. These devices often carry out important tasks such as reporting critical information from precise sensors and monitoring power levels in the grid. Because of this, security and stability are paramount. To ensure the stability of these IIOT devices, they must be monitored. By monitoring an IIOT server, you can verify optimal management of CPU, disc, memory resources and network traffic, as well as ensuring a whole assortment of optional and customisable metrics are in check. IIOT devices are often spread across the whole world. Having a monitoring system that is both scalable and secure is of utmost importance. The best way to ensure this is by hosting it in the cloud. The cloud is becoming the new normal for server solutions, due to the low cost, ease of deployment, high flexibility and low maintenance. 

Many of the solutions to this problem are provided by expensive enterprise applications and frameworks which require licensing on a per node basis as well as yearly maintenance fees. As well as the upfront fees and annual costs, these products often tie you into a large ecosystem of proprietary additional applications, modules, adaptors and extensions. This makes it difficult to freely innovate and adapt. By using a suite of free open-source, customisable and specially curated software, programming languages and tools, a novel solution can be built to give users a quick, customisable and easy-to-deploy system that provides the same, if not better, experience than that of an expensive enterprise product, combined with the ability to extend or reconfigure at lower cost.
Aims
-	Use a selection of technologies and languages to design and create a deployable cloud-based solution to IIOT server monitoring
-	Implement an intuitive administrator user interface, to enable a user to quickly and easily connect and configure the IIOT endpoints
-	Research and explore IIOT and cloud technologies to find the best solution possible
-	Explore opportunities for large scale IOT testing and simulation
Objectives
Primary
-	The solution must collect server metrics from remote IIOT devices and display them in a customisable graphical interface. This will provide the user with important information about their endpoints, allowing them to ensure security and stability of their system.
-	The solution must allow the user to easily and quickly add IIOT device endpoints to the system, through a simple user interface. Automating the complex and individual node configuration that would otherwise be required. The system will use automation technology to install, configure and scale the required resources.
-	The solution should use a microservices architecture to ensure scalability and stability. Containerisation results in a secure and ready to deploy program. 
-	The solution must collect time series data, stored in a well-designed database that can scale as required.
Extension
-	Research the creation of models to predict and understand patterns of failure in the IIOT devices
-	Use Kubernetes to orchestrate the deployment of the entire system
-	Use and test the final product on a large scale. Simulating 100+ endpoints 

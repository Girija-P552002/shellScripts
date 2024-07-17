#!/bin/bash

java --version
mvn  --version
cd /home/girija/Downloads/springbootmavendemo/src/main/java/com/example/springbootmavendemo

touch RequestMapping.java

echo "package com.example.springbootmavendemo" > RequestMapping.java

echo "public @interface RequestMapping {
}" > RequestMapping.java

touch HelloController.java

echo "package com.example.springbootmavendemo;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
@RestController
public class HelloController {
    @RequestMapping("\"/"\")
    public String index()
    {
        return "\"Hello everyone!! This my simple and first spring boot project"\";
    }

}" > HelloController.java

echo "change the directory where the file is present "


cd /home/girija/Downloads/springbootmavendemo || { echo "Failed to change directory"; exit 0; }

./mvnw install

./mvnw spring-boot:run 

cd target/ ||  exit 0

java -jar springbootmavendemo.jar

echo "Spring Boot project deployment completed successfully."


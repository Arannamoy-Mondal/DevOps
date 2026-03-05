package com.aranna.java_02_hello_world_double_stage;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;



@RestController
public class Test {
    @GetMapping("/test")
    public String getMethodName() {
        return "Ok";
    }
    
}

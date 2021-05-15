package com.antra.report.client.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.AsyncConfigurer;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

import java.util.concurrent.Executor;
import java.util.concurrent.ThreadPoolExecutor;

@Configuration
@EnableAsync
public class AsyncConfig {

    @Bean("asyncTaskExecutor")
    public Executor getAsyncExecutor() {
        ThreadPoolTaskExecutor threadPoolTaskExecutor = new ThreadPoolTaskExecutor();

        threadPoolTaskExecutor.setCorePoolSize(2);

        threadPoolTaskExecutor.setMaxPoolSize(3);

        threadPoolTaskExecutor.setQueueCapacity(50);

        threadPoolTaskExecutor.setThreadNamePrefix("taskExecutor-");

        threadPoolTaskExecutor.initialize();
        return threadPoolTaskExecutor;
    }

}

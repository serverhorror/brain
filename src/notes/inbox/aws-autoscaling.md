---
created: 2026-05-07
id: 6cd80bfb-e3da-4499-9e41-43d6bc4d0b05
tags:
  - misc
  - aws
  - kb
---

# AWS Autoscaling

- [Tutorial: Set up a scaled and load-balanced application](https://docs.aws.amazon.com/autoscaling/ec2/userguide/tutorial-ec2-auto-scaling-load-balancer.html)

## Creating an environment manually

1. SecurityGroup `alb-sg`

    - allow `tcp/80` from `0.0.0.0/0`
    - allow `tcp/443` from `0.0.0.0/0`

2. SecurityGroup `alb-2-app-sg`

    - allow `tcp/80` from self
    - allow `tcp/443` from self

3. TargetGroup

4. LoadBalancer (pointing to TargetGroup)

5. LaunchTemplate

6. Autoscalinggroup

    - Add to sg `alb-2-app-sg`
    - register ASG with TG
    - use **Default** version from

## Using a custom image

1. create separate instance
2. connect via SSH
3. install the `nginx` web server
4. in EC2 create image
5. modify to use new image
6. start instance refresh

## Add a database

1. SG `app-2-db`

2. create instance

3. copy connection information around

    - follow [[aws-autoscaling.md#Using a custom image]] to recreate image
      and renew instances

[aws-autoscaling.md#Using a custom image]: <#Using a custom image> "AWS Autoscaling"

---
id: fbuxij67knvy35xezze0ert
title: AWS AutoScaling
desc: 'Tutorial: Set up a scaled and load-balanced application'
updated: 1684701058861
created: 1684697970837
tags:
  - architecture
  - aws
  - kb
---

* [Tutorial: Set up a scaled and load-balanced application](https://docs.aws.amazon.com/autoscaling/ec2/userguide/tutorial-ec2-auto-scaling-load-balancer.html)

## Creating an environment manually

1. SecurityGroup [SG] `alb-sg`
    * allow `tcp/80` from `0.0.0.0/0`
    * allow `tcp/443` from `0.0.0.0/0`
1. SecurityGroup `alb-2-app-sg`
    * allow `tcp/80` from self
    * allow `tcp/443` from self
1. TargetGroup [TG]
1. LoadBalancer [LB] (pointing to TargetGroup)
1. LaunchTemplate [LT]
1. AutoScalingGroup [ASG]
    * add to sg `alb-2-app-sg`
    * register ASG with TG
    * use _Default_ version from LT

### Using a custom image

1. create separate instance
1. connect via SSH
1. install `nginx`
1. in EC2 create image
1. modify LT to use new image
1. start instance refresh

## Add a database

1. SG `app-2-db`
1. create instance
1. copy connection information around
    * follow _Using a custom image_ to recreate image and
      renew instances
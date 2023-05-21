---
id: fbuxij67knvy35xezze0ert
title: AWS AutoScaling
desc: 'Tutorial: Set up a scaled and load-balanced application'
updated: 1684698357453
created: 1684697970837
---

* [Tutorial: Set up a scaled and load-balanced application](https://docs.aws.amazon.com/autoscaling/ec2/userguide/tutorial-ec2-auto-scaling-load-balancer.html)

## Creating an environment manually

1. SecurityGroup `alb-sg`
    * allow `tcp/80` from `0.0.0.0/0`
    * allow `tcp/443` from `0.0.0.0/0`
1. SecurityGroup `alb-2-app-sg`
    * allow `tcp/80` from self
    * allow `tcp/443` from self
1. TargetGroup
1. LoadBalancer (pointing to TargetGroup)
1. AutoScalingGroup
    * add to sg `alb-2-app-sg`


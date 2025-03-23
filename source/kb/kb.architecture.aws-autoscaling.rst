.. _kb.architecture.aws-autoscaling:

AWS AutoScaling
===============

- `Tutorial: Set up a scaled and load-balanced application <https://docs.aws.amazon.com/autoscaling/ec2/userguide/tutorial-ec2-auto-scaling-load-balancer.html>`_

Creating an environment manually
--------------------------------

#. SecurityGroup [SG] ``alb-sg``

   - allow ``tcp/80`` from ``0.0.0.0/0``
   - allow ``tcp/443`` from ``0.0.0.0/0``

#. SecurityGroup ``alb-2-app-sg``

   - allow ``tcp/80`` from self
   - allow ``tcp/443`` from self

#. TargetGroup [TG]
#. LoadBalancer [LB] (pointing to TargetGroup)
#. LaunchTemplate [LT]
#. AutoScalingGroup [ASG]

   - add to sg ``alb-2-app-sg``
   - register ASG with TG
   - use *Default* version from [LT]

.. _kb.architecture.aws-autoscaling.using-a-custom-image:

Using a custom image
--------------------

#. create separate instance
#. connect via SSH
#. install the :program:`nginx` web server
#. in EC2 create image
#. modify [LT] to use new image
#. start instance refresh

Add a database
--------------

#. SG `app-2-db`
#. create instance
#. copy connection information around

   - follow
     :ref:`kb.architecture.aws-autoscaling.using-a-custom-image`
     to recreate image and renew instances

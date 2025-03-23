.. _kb.git:

Git
===

.. _kb.git.using-bitbucket:

Using **BitBucket Server/Datacenter** Git
=========================================

#. Create a personal access token

#. Do this for your git configuration

   .. code-block:: text
      :linenos:

      git config --global http.https://bitbucket.example.com.extraHeader 'Authorization: Bearer  Token'

   Some more details

   .. code-block:: text
     :linenos:

     git clone -c http.extraHeader='Authorization: Bearer REPLACE_WITH_TOKEN' https://bitbucket.example.com/scm/project-name/repo-name.git
     git config --global http.https://bitbucket.example.com.extraHeader 'Authorization: Bearer  Token'

   *or* (if you don't want to use the token in the header)

   .. code-block:: text
      :linenos:

      git config --global url."https://<username>:<personal-access-token>@bitbucket.example.com".insteadOf "https://bitbucket.example.com"

#. As your module URLs use something like this for :ref:`kb.go` projects:

   - `bitbucket.example.com/project/repo`

     **Do NOT** use the `scm` part in the URL

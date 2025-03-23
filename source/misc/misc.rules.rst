.. _misc-rules:

Rules
-----

.. epigraph::

    .. rubric:: ... on Infrastructure

    - There is one system, not a collection of systems.
    - The desired state of the system should be a known quantity.
    - The "known quantity" must be machine parseable.
    - The actual state of the system must self-correct to the desired state.
    - The only authoritative source for the actual state of the system is the system.
    - The entire system must be deployable using source media and text files.

    .. rubric:: ... on Buying Software

    - Keep the components in the infrastructure simple so it will be better understood.
    - All products must authenticate and authorize from external, configurable sources.
    - Use small tools that interoperate well, not one "do everything poorly" product.
    - Do not implement any product that no one in your organization has administered.
    - "Administered" does not mean saw it in a rigged demo, online or otherwise.
    - If you must deploy the product, hire someone who has implemented it before to do so.

    .. rubric:: ... on Automation

    - Do not author any code you would not buy.
    - Do not implement any product that does not provide an API.
    - The provided API must have all functionality that the application provides.
    - The provided API must be tailored to more than one language and platform.
    - Source code counts as an API, and may be restricted to one language or platform.
    - The API must include functional examples and not require someone to be an expert on the product to use.
    - Do not use any product with configurations that are not machine parseable and machine writeable.
    - All data stored in the product must be machine readable and writeable by applications other than the product itself.
    - Writing hacks around the deficiencies in a product should be less work than writing the product's functionality.

    .. rubric:: ... in general

    - Keep the disparity in your architecture to an absolute minimum.
    - Use `Set Theory <http://en.wikipedia.org/wiki/Set_theory>`_ to accomplish this.
    - Do not improve manual processes if you can automate them instead.
    - Do not buy software that requires bare-metal.
    - Manual data transfers and datastores maintained manually are to be avoided.

_Source: [Rules ...](https://gist.githubusercontent.com/serverhorror/253304/raw/da2c1f329fc85fdfc8906b7569824aeb2e8588a6/rules_on_infrastructure.mdown)_

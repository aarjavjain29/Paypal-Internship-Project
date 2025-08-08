# Onboarding-new-Product-to-UCP
This repository contains the prompts that I used for automating new product onboarding to UCP.

There are two sections. One is prompt1.md, which contains the prompt used for API spec changes, enum updates, and application code changes.

The other is prompt2.md, which contains the prompt used for disposition changes.

# Flow of Automation

Before starting, make sure to set up GitHub and Atlassian MCP servers in VS Code (you can refer to this page for setup: https://paypal.atlassian.net/wiki/spaces/SMBFS/pages/2215246080/MCP+Server+Setup+Guides#Local-Setup-(STDIO)-DEPRECATED).

The first confluence page that I created, named "Onboarding a new product to UCP" under the CreditRisk space (Link: https://paypal.atlassian.net/wiki/spaces/CreditRisk/pages/2581170251/Onboarding+a+New+Product+to+UCP), contains the changes that are required for new product onboarding. It mainly covers instructions for API spec changes for Collections Common Components Specification, Collections Delinquencies Specification, Collections Debt Profile API Specification, Collections Notifications Specification, Collections Placements Specification, Collections Adjustment API Specification, and enum updates changes for Collections Platform Helpers, Collection Interface, and application code changes for AMQCLCTNLIFECYCLED, CLCTNDLNQNCYMGMTSERV, CLCTNNOTIFICATIONSERV, CLCTNPLACEMENTSERV, and CLCTNADJUSTMENTSERV.

All the changes that are required are already mentioned for each repo, but if there are any specific changes that are needed for any repo, then that should be added by the user before starting the automation.

Prompts that are used for above changes

1. Onboard a new product to UCP based on the detailed instructions mentioned in the Confluence page with ID: 2581170251. As part of onboarding, perform only API specs and enum updates for now, and do them in chunks because it may exceed the maximum token limit for a single edit operation.

The above prompt will mostly be done with API specs and enum changes, and after that give a prompt. 

2. Create a master page with all the details that are mentioned in the Confluence page with ID: 2581170251.

It will create a page where all the details of the product will be there, but if any details like product code or country code are not there, then go and manually add them in the master page.

After that, close this session and open a new session. Give a prompt. 

3. Perform only the application code changes that are mentioned in the Confluence page with ID: 2581170251.

After this, all these changes will be done, and a PR will be raised for each of them, and you will also have a master page for that new product that contains all the information of the product.

In between the process, if the agent starts hallucinating, then try to give a finer prompt to it so that it works correctly.


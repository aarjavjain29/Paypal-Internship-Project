# Onboarding New Products to UCP Platform

## Introduction

This page serves as a comprehensive reference for onboarding new products to the UCP platform. It outlines all necessary steps, including updates to API specifications, enum values, and application configuration changes. By following this guide, users can streamline the onboarding process and ensure consistency across the platform.

## Required Input

Ask user to provide the following information about the new product:

1. **Product ID**: Example "PAY_LATER_LONG_TERM_US"
2. **Product ID Description**: Example "The interest bearing loan product for US with relatively longer payback period Installments broken out monthly for a term of upto 48 months"
3. **Product Name**: "PAY_LATER"
4. **Product Name Description**: "Global Pay Later loan"
5. **Jira Ticket Number**: Example "DL-1234"
6. Ask user whether the new product is a completely different product or just expanding the existing one.

## API Specification Updates

### 1. Collections Common Components Specification

**Repository**: https://github.paypal.com/ApiSpecifications-R/collections.CommonComponentsSpecification  
**Owner**: ApiSpecifications-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Fork the repository using #fork_repository tool
2. Clone the forked repo only via SSH command only
3. **Update JSON files**:
   - In both v1/ and v2/ directories:
     - Add product_id and product_id_description in the product_id.json
     - Add product_name and product_name_description in the product_name.json only if user says that this product is completely different product
     - Ensure that the descriptions end with a period
4. **Schema constraint update (if needed)**:
   - If product_id.length > 32, update the maxLength constraint in schema definitions for both v1 and v2
5. **Version bump**:
   - In each pom.xml, bump the patch version (ex. 1.0.61 to 1.0.62)
6. **Commit the Changes**:
   - Use the appropriate small commit message
7. **Push** current branch to forked repository on GitHub
8. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the master branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description of the PR should be short and clear

### 2. Collections Delinquencies Specification

**Repository**: https://github.paypal.com/ApiSpecifications-R/collections.DelinquenciesSpecification/  
**Owner**: ApiSpecifications-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Fork the repository using #fork_repository tool
2. Clone the forked repo only via SSH command only
3. **Branch Selection**:
   - Identify the latest non-archived branch that starts with 'v' (e.g., v1.3.0) and if it exists then switch to it
   - If no such branch exists, prompt the user with: "No active version branch (starting with 'v') found. Please create a new minor version in PPaaS."
4. **In v1/pom.xml file**:
   - Update the collections-common version with the updated value from the PR created above for collections-common spec
   - Increment the patch version of collections-delinquency-api (ex. 1.1.1 to 1.1.2)
5. **Submodule Update Commands** (run in exact order):
   ```bash
   git submodule update --init --recursive
   cd v1/schema/collections_common_components
   git pull origin master
   cd -
   ```
6. **Commit the Changes**: Use appropriate small commit message
7. **Push** current branch to forked repository on GitHub
8. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the latest branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description should be short

### 3. Collections Debt Profile API Specification

**Repository**: https://github.paypal.com/Risk-R/collections.DebtProfileAPISpecification  
**Owner**: Risk-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Fork the repository using #fork_repository tool
2. Clone the forked repo only via SSH command only
3. **Branch Selection**:
   - Identify the latest non-archived branch that starts with 'v' (e.g., v1.3.0) and if it exists then switch to it
   - If no such branch exists, prompt the user with: "No active version branch (starting with 'v') found. Please create a new minor version in PPaaS."
4. **In v1/pom.xml file**:
   - Update the collections-common version with the updated value from the PR created above for collections-common spec
   - Increment the patch version of debtprofile-specification (ex. 1.0.61 to 1.0.62)
5. **Submodule Update Commands** (run in exact order):
   ```bash
   git submodule update --init --recursive
   cd v1/schema/collections_common_components
   git pull origin master
   cd -
   ```
6. **Commit the Changes**: Use appropriate small commit message
7. **Push** current branch to forked repository on GitHub
8. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the latest branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description should be short

### 4. Collections Notifications Specification

**Repository**: https://github.paypal.com/ApiSpecifications-R/collections.NotificationsSpecification  
**Owner**: ApiSpecifications-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Fork the repository using #fork_repository tool
2. Clone the forked repo only via SSH command only
3. **Branch Selection**:
   - Identify the latest non-archived branch that starts with 'v' (e.g., v1.3.0) and if it exists then switch to it
   - If no such branch exists, prompt the user with: "No active version branch (starting with 'v') found. Please create a new minor version in PPaaS."
4. **In v2/pom.xml file**:
   - Update the collections-common version with the updated value from the PR created above for collections-common spec
   - Increment the patch version of collections-notification-api (ex. 2.12 to 2.12.1)
5. **Submodule Update Commands** (run in exact order):
   ```bash
   git submodule update --init --recursive
   cd v1/schema/collections_common_components
   git pull origin master
   cd -
   ```
6. **Commit the Changes**: Use appropriate small commit message
7. **Push** current branch to forked repository on GitHub
8. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the latest branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description should be short

### 5. Collections Placements Specification

**Repository**: https://github.paypal.com/ApiSpecifications-R/collections.PlacementsSpecification  
**Owner**: ApiSpecifications-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Fork the repository using #fork_repository tool
2. Clone the forked repo only via SSH command only
3. **Branch Selection**:
   - Identify the latest non-archived branch that starts with 'v' (e.g., v1.3.0) and if it exists then switch to it
   - If no such branch exists, prompt the user with: "No active version branch (starting with 'v') found. Please create a new minor version in PPaaS."
4. **In the root pom.xml file**:
   - Increment the minor version of collections-placements-parent and add the suffix -SNAPSHOT to it
5. **In the v2/pom.xml file**:
   - Update the collections-common version with the updated value from the PR created above for collections-common spec
   - Increment the minor version collections-placements-api and collections-placements-parent and add the suffix -SNAPSHOT to them (ex. 2.9.0 to 2.10.0-SNAPSHOT)
6. **Submodule Update Commands** (run in exact order):
   ```bash
   git submodule update --init --recursive
   cd v1/schema/collections_common_components
   git pull origin master
   cd -
   ```
7. **Commit the Changes**: Use appropriate small commit message
8. **Push** current branch to forked repository on GitHub
9. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the latest branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description should be short

### 6. Collections Adjustment API Specification

**Repository**: https://github.paypal.com/ApiSpecifications-R/collections.AdjustmentAPISpecification  
**Owner**: ApiSpecifications-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Fork the repository using #fork_repository tool
2. Clone the forked repo only via SSH command only
3. **Branch Selection**:
   - Identify the latest non-archived branch that starts with 'v' (e.g., v1.3.0) and if it exists then switch to it
   - If no such branch exists, prompt the user with: "No active version branch (starting with 'v') found. Please create a new minor version in PPaaS."
4. **In v1/pom.xml file**:
   - Update the collections-common version with the updated value from the PR created above for collections-common spec
   - Increment the patch version of adjustments-api (ex. 1.1.1 to 1.1.2)
5. **Submodule Update Commands** (run in exact order):
   ```bash
   git submodule update --init --recursive
   cd v1/schema/collections_common_components
   git pull origin master
   cd -
   ```
6. **Commit the Changes**: Use appropriate small commit message
7. **Push** current branch to forked repository on GitHub
8. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the latest branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description should be short

## Enums Updates

### 1. Collections Platform Helpers

**Repository**: https://github.paypal.com/Risk-R/collections-platform-helpers  
**Owner**: Risk-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Clone the repo without forking and only via SSH command only
2. **Create a Feature Branch**:
   - Create and switch to a new branch with the format: `feature/{PRODUCT_ID}`
3. **Update Files**:
   - Update the collections-common version with the updated value from the PR created above for collections-common spec
   - Add the product_id to productId.java file, if you require any information then prompt the user to provide it
4. **Commit the Changes**: Use appropriate small commit message
5. **Push** current branch to forked repository on GitHub
6. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the latest branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description should be short

### 2. Collection Interface

**Repository**: https://github.paypal.com/Risk-R/collection-interface  
**Owner**: Risk-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Fork the repository using #fork_repository tool
2. Clone the forked repo and only via SSH command only
3. **Create a Feature Branch**:
   - Create and switch to a new branch with the format: `feature/{PRODUCT_ID}`
4. **Update Files**:
   - Add the product_id in the CollectionProductId.oml file
   - Add the product_name in the CollectionProduct.oml file
   - Increment the patch version of collection-interface in the root pom.xml file (ex. 1.0.61 to 1.0.62)
5. **Commit the Changes**: Use appropriate small commit message
6. **Push** current branch to forked repository on GitHub
7. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the latest branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description should be short

## Creating a Master Page for the Product

Create a Confluence page under CreditRisk space whose title should be "Onboarding {Product_id} to UCP" where mention each and every information of the product like:
- Product ID
- Product ID Description
- Product Name
- Product Name Description
- Product Country Code
- Product Code
- Jira Ticket

Also mention each version updates along with their name which you made on the above repositories with their respective PR links in a clean and table format.

## Application Code Updates

### 1. AMQCLCTNLIFECYCLED

**Repository**: https://github.paypal.com/Risk-R/amqclctnlifecycled  
**Owner**: Risk-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Clone the forked repo only via SSH command only
2. **Create a Branch**:
   - Create and switch to a new branch with the format: `feature/{JIRA_TICKET}`
3. **Configuration Updates**:
   - Prompt the user: "Is the product impacted by user vulnerability in the UK/GB region?(yes/no)"
   - If the user answers "yes" then strictly add the product_id to the `products.impacted.by.vulnerability` in application.properties
4. **In the root pom.xml file**:
   - Update the collection.interface, collection.common.spec.version and collections.platform.helpers.version with their updated value from the confluence page provided, if you don't find any updated version there then prompt user to provide it
5. **In the /amqclctnlifecycledDaemon/pom.xml file**:
   - Update the collections-notification-api, debtprofile-specification and collections-delinquency-api with their updated value from the confluence page provided, if you don't find any updated version there then prompt user to provide it
6. **Commit the Changes**: Use appropriate small commit message
7. **Push** current branch to forked repository on GitHub
8. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the develop branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description should be short and effective

### 2. CLCTNDLNQNCYMGMTSERV

**Repository**: https://github.paypal.com/Risk-R/clctndlnqncymgmtserv  
**Owner**: Risk-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Clone the forked repo only via SSH command only
2. **Create a Branch**:
   - Create and switch to a new branch with the format: `feature/{JIRA_TICKET}`
3. **Configuration Updates**:
   - Add the product name in valid.products and product id in valid.product.ids in application.properties file
   - Prompt the user: "Is this a multi-cardinal loan product ? (yes/no)"
     - If the user answer "yes" then add the product name to products.for.propagating.disposition and products.for.tagging.associated.delinquencies in application.properties
   - Prompt the user: "Do the product's rules require historical notification details for evaluation ?(yes/no)"
     - If the user answer "yes" then add the product name to notification.history.enabled.products in application.properties
   - Prompt the user: "Is this product being marketed in the UK region and required to honor user vulnerabilities ? (yes/no)"
     - If the user answer "yes" then add the product name to user.vulnerabilities.valid.products in application.properties
4. **In the root pom.xml file**:
   - Update the collections-delinquency-api, collection.common.spec.version and collections.platform.helpers.version with their updated value from the confluence page provided, if you don't find any updated version there then prompt user to provide it
5. **In the /clctndlnqncymgmtservService/pom.xml file**:
   - Update the collections-notification-api, debtprofile-specification, collections-placement-api(remove SNAPSHOT while updating) and collection-interface with their updated value from the confluence page provided, if you don't find any updated version there then prompt user to provide it
6. **Commit the Changes**: Use appropriate small commit message
7. **Push** current branch to forked repository on GitHub
8. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the develop branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description should be short and effective

### 3. CLCTNNOTIFICATIONSERV

**Repository**: https://github.paypal.com/Risk-R/clctnnotificationserv  
**Owner**: Risk-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Clone the forked repo only via SSH command only
2. **Create a Branch**:
   - Create and switch to a new branch with the format: `feature/{JIRA_TICKET}`
3. **Configuration Updates**:
   - Add the product name in valid.products and product id in valid.product.ids in application.properties file
4. **In the root pom.xml file**:
   - Update the collections.notification.spec.version, collection.common.spec.version and collections.platform.helpers.version with their updated value from the confluence page provided, if you don't find any updated version there then prompt user to provide it
5. **In the /clctnnotificationservService/pom.xml file**:
   - Update the collections-notification-api, debtprofile-specification, collections-placement-api(remove SNAPSHOT while updating) and collection-interface with their updated value from the confluence page provided, if you don't find any updated version there then prompt user to provide it
6. **Commit the Changes**: Use appropriate small commit message
7. **Push** current branch to forked repository on GitHub
8. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the develop branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description should be short and effective

### 4. CLCTNPLACEMENTSERV

**Repository**: https://github.paypal.com/Risk-R/clctnplacementserv  
**Owner**: Risk-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Clone the forked repo only via SSH command only
2. **Create a Branch**:
   - Create and switch to a new branch with the format: `feature/{JIRA_TICKET}`
3. **Configuration Updates**:
   - Add the product name in valid.products and product id in valid.product.ids, phone.transformation.eligible.product.ids and product.ids.generate.old.format.data.in.transformed.file in application.properties
   - Prompt the user: "Does this product require historical notification tracking (to verify if the first collections notification has been sent)? (yes/no)"
     - If the user answer "yes" then add the product name to {#product_code}.notification.history.enabled.products in application.properties and fetch the appropriate product_code according to product_name from https://github.paypal.com/Risk-R/collections-platform-helpers/blob/develop/collections-domain-objects/src/main/java/com/paypal/collections/common/ProductName.java
   - Prompt the user: "Is this a LONG TERM product being introduced in a geography where a short-term equivalent already exists?(yes/no)"
     - If the user answer "yes" then add the product id to product.ids.required.to.fetch.metadata in application.properties
   - Prompt the user: "Do placements for this product require loading of communication preferences? (yes/no)"
     - If the user answer "yes" then add the product name to products.communication.preferences.enabled in application.properties
4. **In the root pom.xml file**:
   - Update the collections.placement.spec.version ,collection.common.spec.version and collections.platform.helpers.version with their updated value from the confluence page provided, if you don't find any updated version there then prompt user to provide it
5. **In the /clctnplacementservService/pom.xml file**:
   - Update the debtprofile-specification and collection-interface with their updated value from the confluence page provided, if you don't find any updated version there then prompt user to provide it
6. **Commit the Changes**: Use appropriate small commit message
7. **Push** current branch to forked repository on GitHub
8. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the develop branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description should be short and effective

### 5. CLCTNADJUSTMENTSERV

**Repository**: https://github.paypal.com/Risk-R/clctnadjustmentserv  
**Owner**: Risk-R (PayPal GitHub Enterprise Server: github.paypal.com)

#### Steps:
1. Clone the forked repo only via SSH command only
2. **Create a Branch**:
   - Create and switch to a new branch with the format: `feature/{JIRA_TICKET}`
3. **Configuration Updates**:
   - Add product name to valid.products in application.properties file
4. **In the /clctnadjustmentserv/pom.xml file**:
   - Update the collections.platform.helpers.version , collection.common.spec.version and adjustments.api.spec.version with their updated value from the confluence page provided, if you don't find any updated version there then prompt user to provide it
5. **Commit the Changes**: Use appropriate small commit message
6. **Push** current branch to forked repository on GitHub
7. **PR Creation**:
   - Create a GitHub Pull Request from current branch to the develop branch of the original repository
   - Use the format: "{JIRA_TICKET_NO} Onboarding {Product_ID} to UCP" for PR
   - The description should be short and effective
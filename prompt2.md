# Database SQL Scripts Generation for Disposition changes

## Introduction

This document provides comprehensive instructions for generating SQL scripts (APPLYSQL, VERIFY, and ROLLBACK) for four database tables required for UCP onboarding. Each table requires three types of scripts to ensure proper database operations and rollback capabilities.

## Common Configuration

### Author Information
For all scripts, I used the following author details:

1. **Author(s)**: "Aarjav Jain"
2. **Contact Work Email**: aarjjain@paypal.com
3. **Contact Work Phone**: +91-7417223185
4. **Manager Work Email**: Dinesh Srinivasan (disrinivasan@paypal.com)
5. **Manager Work Phone**: +91-7760108606

### Reference Information
- **Reference SDS Ticket**: "SDS-12345"
- **Source Confluence Page ID**: 2625073341
- **Target Confluence Page ID**: 2625281054

## Table 1: T_DSPTN_PROD_TYP_LKP

### Description
Generate all three SQL scripts for the T_DSPTN_PROD_TYP_LKP Table mentioned in the confluence page with ID: 2625073341.

**Reference SDS Ticket**: "SDS-12345"

### APPLYSQL Script
- **Template Source**: Use #get_file_contents on https://github.paypal.com/aradsingh/db-2025-04/blob/86711e25fa2680cdca1f44fa8d359b0e033ae148/CLCTN/SDS-36563/APPLYSQL.SDS-36563.INSERT_T_DSPTN_PROD_TYP_LKP.4.sql
- **Output File**: CLCTN/SDS-TICKET/APPLYSQL.SDS-TICKET.INSERT_T_DSPTN_PROD_TYP_LKP.sql

### VERIFY Script
- **Template Source**: Use #get_file_contents on https://github.paypal.com/aradsingh/db-2025-04/blob/86711e25fa2680cdca1f44fa8d359b0e033ae148/CLCTN/SDS-36563/VERIFY.SDS-36563.INSERT_T_DSPTN_PROD_TYP_LKP.5.sql
- **Output File**: CLCTN/SDS-TICKET/VERIFY.SDS-TICKET.INSERT_T_DSPTN_PROD_TYP_LKP.sql

### ROLLBACK Script
- **Template Source**: Use #get_file_contents on https://github.paypal.com/aradsingh/db-2025-04/blob/86711e25fa2680cdca1f44fa8d359b0e033ae148/CLCTN/SDS-36563/ROLLBACK.SDS-36563.INSERT_T_DSPTN_PROD_TYP_LKP.sql
- **Output File**: CLCTN/SDS-TICKET/ROLLBACK.SDS-TICKET.INSERT_T_DSPTN_AGENT_ROLE_DSPTN_LKP.sql

### Data Processing Instructions
- Retain the original structure but replace INSERT/VERIFY/ROLLBACK statements with data from T_DSPTN_PROD_TYP_LKP Table
- Fetch data via #confluence_get_page for page with ID: 2625073341
- Update the T_DSPTN_PROD_TYP_LKP Table mentioned in confluence page ID: 2625281054 with new DSPTN_PROD_TYP_ID and DSPTN_PROD_TYP_CD

## Table 2: T_DSPTN_AGENT_ROLE_LKP

### Description
Generate all three SQL scripts for the T_DSPTN_AGENT_ROLE_LKP Table mentioned in the confluence page with ID: 2625073341.

**Reference SDS Ticket**: "SDS-12345"

### APPLYSQL Script
- **Template Source**: Use #get_file_contents on https://github.paypal.com/aradsingh/db-2025-04/blob/86711e25fa2680cdca1f44fa8d359b0e033ae148/CLCTN/SDS-36563/APPLYSQL.SDS-36563.INSERT_T_DSPTN_AGENT_ROLE_LKP.7.sql
- **Output File**: CLCTN/SDS-TICKET/APPLYSQL.SDS-TICKET.INSERT_T_DSPTN_AGENT_ROLE_LKP.sql

### VERIFY Script
- **Template Source**: Use #get_file_contents on https://github.paypal.com/aradsingh/db-2025-04/blob/86711e25fa2680cdca1f44fa8d359b0e033ae148/CLCTN/SDS-36563/VERIFY.SDS-36563.INSERT_T_DSPTN_AGENT_ROLE_LKP.8.sql
- **Output File**: CLCTN/SDS-TICKET/VERIFY.SDS-TICKET.INSERT_T_DSPTN_AGENT_ROLE_LKP.sql

### ROLLBACK Script
- **Template Source**: Use #get_file_contents on https://github.paypal.com/aradsingh/db-2025-04/blob/86711e25fa2680cdca1f44fa8d359b0e033ae148/CLCTN/SDS-36563/ROLLBACK.SDS-36563.INSERT_T_DSPTN_AGENT_ROLE_LKP.9.sql
- **Output File**: CLCTN/SDS-TICKET/ROLLBACK.SDS-TICKET.INSERT_T_DSPTN_AGENT_ROLE_LKP.sql

### Data Processing Instructions
- Retain the original structure but replace INSERT/VERIFY/ROLLBACK statements with data from T_DSPTN_AGENT_ROLE_LKP Table
- Fetch data via #confluence_get_page for page with ID: 2625073341
- If new DSPTN_AGENT_ROLE_ID created, insert that entry in the T_DSPTN_AGENT_ROLE_LKP Table mentioned in confluence page ID: 2625281054
- Also update the DSPTN_AGENT_ROLE_ID column in the T_DSPTN_AGENT_ROLE_DSPTN_LKP Table

## Table 3: T_DSPTN_AGENT_ROLE_DSPTN_LKP

### Description
Generate all three SQL scripts for the T_DSPTN_AGENT_ROLE_DSPTN_LKP Table mentioned in the confluence page with ID: 2625073341.

**Reference SDS Ticket**: "SDS-12345"

### APPLYSQL Script
- **Template Source**: Use #get_file_contents on https://github.paypal.com/aradsingh/db-2025-04/blob/86711e25fa2680cdca1f44fa8d359b0e033ae148/CLCTN/SDS-36563/APPLYSQL.SDS-36563.INSERT_T_DSPTN_AGENT_ROLE_DSPTN_LKP.13.sql
- **Output File**: CLCTN/SDS-TICKET/APPLYSQL.SDS-TICKET.INSERT_T_DSPTN_AGENT_ROLE_DSPTN_LKP.sql

### VERIFY Script
- **Template Source**: Use #get_file_contents on https://github.paypal.com/aradsingh/db-2025-04/blob/86711e25fa2680cdca1f44fa8d359b0e033ae148/CLCTN/SDS-36563/VERIFY.SDS-36563.INSERT_T_DSPTN_AGENT_ROLE_DSPTN_LKP.14.sql
- **Output File**: CLCTN/SDS-TICKET/VERIFY.SDS-TICKET.INSERT_T_DSPTN_AGENT_ROLE_DSPTN_LKP.sql

### ROLLBACK Script
- **Template Source**: Use #get_file_contents on https://github.paypal.com/aradsingh/db-2025-04/blob/86711e25fa2680cdca1f44fa8d359b0e033ae148/CLCTN/SDS-36563/ROLLBACK.SDS-36563.INSERT_T_DSPTN_AGENT_ROLE_DSPTN_LKP.15.sql
- **Output File**: CLCTN/SDS-TICKET/ROLLBACK.SDS-TICKET.INSERT_T_DSPTN_AGENT_ROLE_DSPTN_LKP.sql

### Data Processing Instructions
- Retain the original structure but replace INSERT/VERIFY/ROLLBACK statements with data from T_DSPTN_AGENT_ROLE_DSPTN_LKP Table
- Fetch data via #confluence_get_page for page with ID: 2625073341
- Generate all insertions for this table and don't stop until all insertions are completed

### Batch Processing Requirements
⚠️ **Important**: The insertion entries are quite large and will exceed the maximum token limit for a single edit operation.

**Processing Strategy**:
- Break insertions into smaller, manageable chunks
- Insert entries in batches of 25
- Process: Insert first 25 entries, then edit the same file to insert the next set of entries
- Continue until all entries are processed

## Table 4: T_DSPTN_LKP

### Description
Generate all three SQL scripts for the T_DSPTN_LKP Table mentioned in the confluence page with ID: 2625073341.

**Reference SDS Ticket**: "SDS-12345"

### APPLYSQL Script
- **Template Source**: Use #get_file_contents on https://github.paypal.com/aradsingh/db-2025-04/blob/86711e25fa2680cdca1f44fa8d359b0e033ae148/CLCTN/SDS-36563/APPLYSQL.SDS-36563.INSERT_T_DSPTN_LKP.10.sql
- **Output File**: CLCTN/SDS-TICKET/APPLYSQL.SDS-TICKET.INSERT_T_DSPTN_LKP.sql

### VERIFY Script
- **Template Source**: Use #get_file_contents on https://github.paypal.com/aradsingh/db-2025-04/blob/86711e25fa2680cdca1f44fa8d359b0e033ae148/CLCTN/SDS-36563/VERIFY.SDS-36563.INSERT_T_DSPTN_LKP.11.sql
- **Output File**: CLCTN/SDS-TICKET/VERIFY.SDS-TICKET.INSERT_T_DSPTN_LKP.sql

### ROLLBACK Script
- **Template Source**: Use #get_file_contents on https://github.paypal.com/aradsingh/db-2025-04/blob/86711e25fa2680cdca1f44fa8d359b0e033ae148/CLCTN/SDS-36563/ROLLBACK.SDS-36563.INSERT_T_DSPTN_LKP.12.sql
- **Output File**: CLCTN/SDS-TICKET/ROLLBACK.SDS-TICKET.INSERT_T_DSPTN_LKP.sql

### Data Processing Instructions
- Retain the original structure but replace INSERT/VERIFY/ROLLBACK statements with data from T_DSPTN_LKP Table
- Fetch data via #confluence_get_page for page with ID: 2625073341

### Batch Processing Requirements
⚠️ **Important**: The insertion entries are quite large and will exceed the maximum token limit for a single edit operation.

**Processing Strategy**:
- Break insertions into smaller, manageable chunks
- Insert entries in batches of 25
- Process: Insert first 25 entries, then edit the same file to insert the next set of entries
- Continue until all entries are processed

## Summary

This document outlines the generation of **12 SQL scripts total** (3 scripts × 4 tables):

1. **T_DSPTN_PROD_TYP_LKP**: 3 scripts (APPLYSQL, VERIFY, ROLLBACK)
2. **T_DSPTN_AGENT_ROLE_LKP**: 3 scripts (APPLYSQL, VERIFY, ROLLBACK)
3. **T_DSPTN_AGENT_ROLE_DSPTN_LKP**: 3 scripts (APPLYSQL, VERIFY, ROLLBACK)
4. **T_DSPTN_LKP**: 3 scripts (APPLYSQL, VERIFY, ROLLBACK)

Each script must follow the template structure while incorporating the specific table data from the designated Confluence pages, with proper author attribution and batch processing for large datasets.
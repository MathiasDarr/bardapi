#!/bin/sh
psql -c "DROP DATABASE IF EXISTS bard_test;" $BARD_DATABASE_URI
psql -c "CREATE DATABASE bard_test;" $BARD_DATABASE_URI
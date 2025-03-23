//go:build tools
// +build tools

package main

//go:generate go install github.com/jstemmer/go-junit-report/v2@latest

import (
	_ "github.com/jstemmer/go-junit-report/v2"
)

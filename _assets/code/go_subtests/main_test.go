package main_test

import (
	"fmt"
	"testing"
)

func divisableByTwo(v int) error {
	if v%2 != 0 {
		return fmt.Errorf("not divisible by two")
	}
	return nil
}

func TestTICKET123(t *testing.T) {
	tc := []struct {
		v       int
		wantErr bool
	}{
		{v: 1, wantErr: true},
		{v: 2, wantErr: false},
	}
	for idx, tt := range tc {
		tName := fmt.Sprintf("Test-%d", idx)
		t.Run(tName, func(t *testing.T) {
			if err := divisableByTwo(tt.v); (err != nil) && !tt.wantErr {
				t.Error(err)
			}
		})
	}
}

def gen_td(n):
	return """
	// entity 0
	{{
	"classname" "func_group"
	"_tb_type" "_tb_group"
	"_tb_name" "td{0}"
	"_tb_id" "1"
	"_tb_linked_group_id" "{{129885a0-4c01-4548-aae4-038d0307d1dd}}"
	}}
	// entity 1
	{{
	"classname" "target_lock"
	"origin" "-664 -4 40"
	"spawnflags" "4"
	"target" "td{0}"
	"targetname" "fn_unlock_td{0}"
	"_tb_group" "1"
	}}
	// entity 2
	{{
	"classname" "trigger_relay"
	"origin" "-664 -4 40"
	"targetname" "fn_unlock_td{0}"
	"message" "fn_unlock_td{0}"
	"_tb_group" "1"
	}}
	// entity 3
	{{
	"classname" "trigger_relay"
	"origin" "-664 -4 40"
	"targetname" "fn_pick_td{0}"
	"message" "fn_pick_td{0}"
	"delay" ".01"
	"target" "fn_unlock_td{0}"
	"_tb_group" "1"
	}}
	// entity 4
	{{
	"classname" "target_lock"
	"origin" "-664 -4 40"
	"spawnflags" "2"
	"target" "td{0}"
	"targetname" "fn_lock_all"
	"_tb_group" "1"
	}}
	// entity 5
	{{
	"classname" "trigger_relay"
	"origin" "-664 -4 40"
	"targetname" "fn_pick"
	"target" "fn_lock_all"
	"target2" "fn_pick_td{0}"
	"_tb_group" "1"
	}}
	// entity 6
	{{
	"classname" "info_teleport_target"
	"origin" "-664 -4 40"
	"targetname" "td{0}"
	"spawnflags" "16"
	"target" "_on_level_enter"
	"message" "td{0}"
	"_tb_group" "1"
	}}
	""".format(n)

import sys
print(gen_td(int(sys.argv[1])))
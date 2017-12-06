%define device z2_plus
%define vendor zuk
%define vendor_pretty ZUK
%define device_pretty ZUK-Alpha
%define installable_zip 1
%define droid_target_aarch64 1

%define straggler_files \
 /init.qcom.sh\
 /init.qcom.usb.sh
%{nil}


%include rpm/dhd/droid-hal-device.inc

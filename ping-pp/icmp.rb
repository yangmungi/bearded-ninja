#!/usr/bin/env ruby

class ICMP
  #
  # Build-control-messages helpers
  #
  def self.basic_control_message(desc_sym, value)
    CONTROL_MESSAGES[desc_sym] = {
      :value => value
    }
  end

  def self.control_message(desc_sym, value, codes=nil)
    self.basic_control_message(desc_sym, value)

    if codes.nil? then
      codes = [desc_sym]
    end

    CONTROL_MESSAGES[desc_sym][:codes] = codes
  end

  CONTROL_MESSAGES = { }

  #
  # Build control messages
  #

  control_message(:echo_reply, 0)
  # 1 reserved
  # 2 reserved
  control_message(:destination_unreachable, 3, [
        :dest_network_ur,        # destination network unreachable
        :dest_host_ur,           # " host "
        :dest_proto_ur,          # " protocol "
        :dest_port_ur,           # " port "
        :fragmentation_required, # fragmentation required and DF flag set
        :src_rt_failed,          # source route failed
        :dest_network_unk,       # destination network unknown
        :dest_host_unk,          # " host " 
        :src_host_iso,           # source host isolated
        :network_admin_proh,     # network administratively prohibited
        :host_admin_proh,        # host " "
        :netowrk_ur_tos,         # network unreachable for TOS
        :host_ur_tos,            # host " " " 
        :comm_admin_prh,         # communication administratively prohibited
        :host_prec_vio,          # host precedence violation
        :prec_cutoff_ie,         # precedence cutoff in effect
      ])
  control_message(:source_quench, 4)
  control_message(:redirect_message, 5, [
        :for_network,
        :for_host,
        :for_tos_network,
        :for_tos_host,
      ])
  basic_control_message(:alternate_host_addr, 6)
  # 7 reserved
  control_message(:echo_request, 8)
  control_message(:router_advertisement, 9)
  control_message(:router_soliciation, 10)
  control_message(:time_exceeded, 11, [
      :ttl_expired,
      :frag_reass_te,
    ])
  control_message(:bad_ip_header, 12, [
      :pointer,
      :missing,
      :bad_length,
    ])
  control_message(:timestamp, 13)
  control_message(:timestamp_reply, 14)
  control_message(:information_request, 15)
  control_message(:information_reply, 16)
  control_message(:addr_mask_request, 17)
  control_message(:addr_mask_reply, 18)

  basic_control_message(:reserved_for_security, 19)

  CONTROL_MESSAGES[:reserved_for_robustness] = { :values => [] }
  (20..29).each do |reserved_code|
    CONTROL_MESSAGES[:reserved_for_robustness][:values] << reserved_code
  end

  control_message(:traceroute, 30, [:information_request])
  basic_control_message(:datagram_conversion_error, 31)
  basic_control_message(:mobile_host_redirect, 32)

  basic_control_message(:where_are_you, 33)
  basic_control_message(:here_i_am, 34)

  basic_control_message(:mobile_registration_request, 35)
  basic_control_message(:mobile_registration_reply, 36)
  basic_control_message(:domain_name_request, 37)
  basic_control_message(:domain_name_reply, 38)
  basic_control_message(:domain_name_reply, 38)

  basic_control_message(:skip_adp, 39)
  basic_control_message(:photuis_security_failures, 40)
  basic_control_message(:icmp_expirimental, 41)

  CONTROL_MESSAGES[:reserved] = { :values => [] }

  [1, 2, 7].each do |reserved_code|
    CONTROL_MESSAGES[:reserved][:values] << reserved_code
  end

  (42..255).each do |reserved_code|
    CONTROL_MESSAGES[:reserved][:values] << reserved_code
  end

  def self.from_str(str)
    
  end
end

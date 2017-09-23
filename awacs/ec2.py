# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon EC2 Spot Fleet'
prefix = 'ec2'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelSpotFleetRequests = Action('CancelSpotFleetRequests')
DescribeSpotFleetInstances = Action('DescribeSpotFleetInstances')
DescribeSpotFleetRequestHistory = \
    Action('DescribeSpotFleetRequestHistory')
DescribeSpotFleetRequests = Action('DescribeSpotFleetRequests')
ModifySpotFleetRequest = Action('ModifySpotFleetRequest')
RequestSpotFleet = Action('RequestSpotFleet')
AcceptReservedInstancesExchangeQuote = \
    Action('AcceptReservedInstancesExchangeQuote')
AcceptVpcPeeringConnection = Action('AcceptVpcPeeringConnection')
AllocateAddress = Action('AllocateAddress')
AllocateHosts = Action('AllocateHosts')
AssignIpv6Addresses = Action('AssignIpv6Addresses')
AssignPrivateIpAddresses = Action('AssignPrivateIpAddresses')
AssociateAddress = Action('AssociateAddress')
AssociateDhcpOptions = Action('AssociateDhcpOptions')
AssociateIamInstanceProfile = Action('AssociateIamInstanceProfile')
AssociateRouteTable = Action('AssociateRouteTable')
AttachClassicLinkVpc = Action('AttachClassicLinkVpc')
AttachInternetGateway = Action('AttachInternetGateway')
AttachNetworkInterface = Action('AttachNetworkInterface')
AttachVolume = Action('AttachVolume')
AttachVpnGateway = Action('AttachVpnGateway')
AuthorizeSecurityGroupEgress = Action('AuthorizeSecurityGroupEgress')
AuthorizeSecurityGroupIngress = Action('AuthorizeSecurityGroupIngress')
BundleInstance = Action('BundleInstance')
CancelBundleTask = Action('CancelBundleTask')
CancelConversionTask = Action('CancelConversionTask')
CancelExportTask = Action('CancelExportTask')
CancelImportTask = Action('CancelImportTask')
CancelReservedInstancesListing = Action('CancelReservedInstancesListing')
CancelSpotFleetRequests = Action('CancelSpotFleetRequests')
CancelSpotInstanceRequests = Action('CancelSpotInstanceRequests')
ConfirmProductInstance = Action('ConfirmProductInstance')
CopyImage = Action('CopyImage')
CopySnapshot = Action('CopySnapshot')
CreateCustomerGateway = Action('CreateCustomerGateway')
CreateDhcpOptions = Action('CreateDhcpOptions')
CreateFlowLogs = Action('CreateFlowLogs')
CreateFpgaImage = Action('CreateFpgaImage')
CreateImage = Action('CreateImage')
CreateInstanceExportTask = Action('CreateInstanceExportTask')
CreateInternetGateway = Action('CreateInternetGateway')
CreateKeyPair = Action('CreateKeyPair')
CreateNatGateway = Action('CreateNatGateway')
CreateNetworkAcl = Action('CreateNetworkAcl')
CreateNetworkAclEntry = Action('CreateNetworkAclEntry')
CreateNetworkInterface = Action('CreateNetworkInterface')
CreateNetworkInterfacePermission = \
    Action('CreateNetworkInterfacePermission')
CreatePlacementGroup = Action('CreatePlacementGroup')
CreateReservedInstancesListing = Action('CreateReservedInstancesListing')
CreateRoute = Action('CreateRoute')
CreateRouteTable = Action('CreateRouteTable')
CreateSecurityGroup = Action('CreateSecurityGroup')
CreateSnapshot = Action('CreateSnapshot')
CreateSpotDatafeedSubscription = Action('CreateSpotDatafeedSubscription')
CreateSubnet = Action('CreateSubnet')
CreateTags = Action('CreateTags')
CreateVolume = Action('CreateVolume')
CreateVpc = Action('CreateVpc')
CreateVpcEndpoint = Action('CreateVpcEndpoint')
CreateVpcPeeringConnection = Action('CreateVpcPeeringConnection')
CreateVpnConnection = Action('CreateVpnConnection')
CreateVpnConnectionRoute = Action('CreateVpnConnectionRoute')
CreateVpnGateway = Action('CreateVpnGateway')
DeleteCustomerGateway = Action('DeleteCustomerGateway')
DeleteDhcpOptions = Action('DeleteDhcpOptions')
DeleteFlowLogs = Action('DeleteFlowLogs')
DeleteInternetGateway = Action('DeleteInternetGateway')
DeleteKeyPair = Action('DeleteKeyPair')
DeleteNatGateway = Action('DeleteNatGateway')
DeleteNetworkAcl = Action('DeleteNetworkAcl')
DeleteNetworkAclEntry = Action('DeleteNetworkAclEntry')
DeleteNetworkInterface = Action('DeleteNetworkInterface')
DeletePlacementGroup = Action('DeletePlacementGroup')
DeleteRoute = Action('DeleteRoute')
DeleteRouteTable = Action('DeleteRouteTable')
DeleteSecurityGroup = Action('DeleteSecurityGroup')
DeleteSnapshot = Action('DeleteSnapshot')
DeleteSpotDatafeedSubscription = Action('DeleteSpotDatafeedSubscription')
DeleteSubnet = Action('DeleteSubnet')
DeleteTags = Action('DeleteTags')
DeleteVolume = Action('DeleteVolume')
DeleteVpc = Action('DeleteVpc')
DeleteVpcEndpoints = Action('DeleteVpcEndpoints')
DeleteVpcPeeringConnection = Action('DeleteVpcPeeringConnection')
DeleteVpnConnection = Action('DeleteVpnConnection')
DeleteVpnConnectionRoute = Action('DeleteVpnConnectionRoute')
DeleteVpnGateway = Action('DeleteVpnGateway')
DeregisterImage = Action('DeregisterImage')
DescribeAccountAttributes = Action('DescribeAccountAttributes')
DescribeAddresses = Action('DescribeAddresses')
DescribeAvailabilityZones = Action('DescribeAvailabilityZones')
DescribeBundleTasks = Action('DescribeBundleTasks')
DescribeClassicLinkInstances = Action('DescribeClassicLinkInstances')
DescribeConversionTasks = Action('DescribeConversionTasks')
DescribeCustomerGateways = Action('DescribeCustomerGateways')
DescribeDhcpOptions = Action('DescribeDhcpOptions')
DescribeEgressOnlyInternetGateways = \
    Action('DescribeEgressOnlyInternetGateways')
DescribeExportTasks = Action('DescribeExportTasks')
DescribeFlowLogs = Action('DescribeFlowLogs')
DescribeFpgaImages = Action('DescribeFpgaImages')
DescribeHostReservationOfferings = \
    Action('DescribeHostReservationOfferings')
DescribeHostReservations = Action('DescribeHostReservations')
DescribeHosts = Action('DescribeHosts')
DescribeIamInstanceProfileAssociations = \
    Action('DescribeIamInstanceProfileAssociations')
DescribeIdFormat = Action('DescribeIdFormat')
DescribeIdentityIdFormat = Action('DescribeIdentityIdFormat')
DescribeImageAttribute = Action('DescribeImageAttribute')
DescribeImages = Action('DescribeImages')
DescribeImportImageTasks = Action('DescribeImportImageTasks')
DescribeImportSnapshotTasks = Action('DescribeImportSnapshotTasks')
DescribeInstanceAttribute = Action('DescribeInstanceAttribute')
DescribeInstanceStatus = Action('DescribeInstanceStatus')
DescribeInstances = Action('DescribeInstances')
DescribeInternetGateways = Action('DescribeInternetGateways')
DescribeKeyPairs = Action('DescribeKeyPairs')
DescribeMovingAddresses = Action('DescribeMovingAddresses')
DescribeNatGateways = Action('DescribeNatGateways')
DescribeNetworkAcls = Action('DescribeNetworkAcls')
DescribeNetworkInterfaceAttribute = \
    Action('DescribeNetworkInterfaceAttribute')
DescribeNetworkInterfaces = Action('DescribeNetworkInterfaces')
DescribePlacementGroups = Action('DescribePlacementGroups')
DescribePrefixLists = Action('DescribePrefixLists')
DescribeRegions = Action('DescribeRegions')
DescribeReservedInstances = Action('DescribeReservedInstances')
DescribeReservedInstancesListings = \
    Action('DescribeReservedInstancesListings')
DescribeReservedInstancesModifications = \
    Action('DescribeReservedInstancesModifications')
DescribeReservedInstancesOfferings = \
    Action('DescribeReservedInstancesOfferings')
DescribeRouteTables = Action('DescribeRouteTables')
DescribeSecurityGroups = Action('DescribeSecurityGroups')
DescribeSnapshotAttribute = Action('DescribeSnapshotAttribute')
DescribeSnapshots = Action('DescribeSnapshots')
DescribeSpotDatafeedSubscription = \
    Action('DescribeSpotDatafeedSubscription')
DescribeSpotFleetInstances = Action('DescribeSpotFleetInstances')
DescribeSpotFleetRequestHistory = \
    Action('DescribeSpotFleetRequestHistory')
DescribeSpotFleetRequests = Action('DescribeSpotFleetRequests')
DescribeSpotInstanceRequests = Action('DescribeSpotInstanceRequests')
DescribeSpotPriceHistory = Action('DescribeSpotPriceHistory')
DescribeStaleSecurityGroups = Action('DescribeStaleSecurityGroups')
DescribeSubnets = Action('DescribeSubnets')
DescribeTags = Action('DescribeTags')
DescribeVolumeAttribute = Action('DescribeVolumeAttribute')
DescribeVolumeStatus = Action('DescribeVolumeStatus')
DescribeVolumes = Action('DescribeVolumes')
DescribeVolumesModifications = Action('DescribeVolumesModifications')
DescribeVpcAttribute = Action('DescribeVpcAttribute')
DescribeVpcClassicLink = Action('DescribeVpcClassicLink')
DescribeVpcClassicLinkDnsSupport = \
    Action('DescribeVpcClassicLinkDnsSupport')
DescribeVpcEndpointServices = Action('DescribeVpcEndpointServices')
DescribeVpcEndpoints = Action('DescribeVpcEndpoints')
DescribeVpcPeeringConnections = Action('DescribeVpcPeeringConnections')
DescribeVpcs = Action('DescribeVpcs')
DescribeVpnConnections = Action('DescribeVpnConnections')
DescribeVpnGateways = Action('DescribeVpnGateways')
DetachClassicLinkVpc = Action('DetachClassicLinkVpc')
DetachInternetGateway = Action('DetachInternetGateway')
DetachNetworkInterface = Action('DetachNetworkInterface')
DetachVolume = Action('DetachVolume')
DetachVpnGateway = Action('DetachVpnGateway')
DisableVgwRoutePropagation = Action('DisableVgwRoutePropagation')
DisableVpcClassicLink = Action('DisableVpcClassicLink')
DisableVpcClassicLinkDnsSupport = \
    Action('DisableVpcClassicLinkDnsSupport')
DisassociateAddress = Action('DisassociateAddress')
DisassociateIamInstanceProfile = Action('DisassociateIamInstanceProfile')
DisassociateRouteTable = Action('DisassociateRouteTable')
DisassociateSubnetCidrBlock = Action('DisassociateSubnetCidrBlock')
DisassociateVpcCidrBlock = Action('DisassociateVpcCidrBlock')
EnableVgwRoutePropagation = Action('EnableVgwRoutePropagation')
EnableVolumeIO = Action('EnableVolumeIO')
EnableVpcClassicLink = Action('EnableVpcClassicLink')
EnableVpcClassicLinkDnsSupport = Action('EnableVpcClassicLinkDnsSupport')
GetConsoleOutput = Action('GetConsoleOutput')
GetConsoleScreenshot = Action('GetConsoleScreenshot')
GetHostReservationPurchasePreview = \
    Action('GetHostReservationPurchasePreview')
GetPasswordData = Action('GetPasswordData')
GetReservedInstancesExchangeQuote = \
    Action('GetReservedInstancesExchangeQuote')
ImportImage = Action('ImportImage')
ImportInstance = Action('ImportInstance')
ImportKeyPair = Action('ImportKeyPair')
ImportSnapshot = Action('ImportSnapshot')
ImportVolume = Action('ImportVolume')
ModifyHosts = Action('ModifyHosts')
ModifyIdFormat = Action('ModifyIdFormat')
ModifyIdentityIdFormat = Action('ModifyIdentityIdFormat')
ModifyImageAttribute = Action('ModifyImageAttribute')
ModifyInstanceAttribute = Action('ModifyInstanceAttribute')
ModifyInstancePlacement = Action('ModifyInstancePlacement')
ModifyNetworkInterfaceAttribute = \
    Action('ModifyNetworkInterfaceAttribute')
ModifyReservedInstances = Action('ModifyReservedInstances')
ModifySnapshotAttribute = Action('ModifySnapshotAttribute')
ModifySpotFleetRequest = Action('ModifySpotFleetRequest')
ModifySubnetAttribute = Action('ModifySubnetAttribute')
ModifyVolume = Action('ModifyVolume')
ModifyVolumeAttribute = Action('ModifyVolumeAttribute')
ModifyVpcAttribute = Action('ModifyVpcAttribute')
ModifyVpcEndpoint = Action('ModifyVpcEndpoint')
ModifyVpcPeeringConnectionOptions = \
    Action('ModifyVpcPeeringConnectionOptions')
MonitorInstances = Action('MonitorInstances')
MoveAddressToVpc = Action('MoveAddressToVpc')
PurchaseHostReservation = Action('PurchaseHostReservation')
PurchaseReservedInstancesOffering = \
    Action('PurchaseReservedInstancesOffering')
PurchaseScheduledInstances = Action('PurchaseScheduledInstances')
RebootInstances = Action('RebootInstances')
RegisterImage = Action('RegisterImage')
RejectVpcPeeringConnection = Action('RejectVpcPeeringConnection')
ReleaseAddress = Action('ReleaseAddress')
ReleaseHosts = Action('ReleaseHosts')
ReplaceIamInstanceProfileAssociation = \
    Action('ReplaceIamInstanceProfileAssociation')
ReplaceNetworkAclAssociation = Action('ReplaceNetworkAclAssociation')
ReplaceNetworkAclEntry = Action('ReplaceNetworkAclEntry')
ReplaceRoute = Action('ReplaceRoute')
ReplaceRouteTableAssociation = Action('ReplaceRouteTableAssociation')
ReportInstanceStatus = Action('ReportInstanceStatus')
RequestSpotFleet = Action('RequestSpotFleet')
RequestSpotInstances = Action('RequestSpotInstances')
ResetImageAttribute = Action('ResetImageAttribute')
ResetInstanceAttribute = Action('ResetInstanceAttribute')
ResetNetworkInterfaceAttribute = Action('ResetNetworkInterfaceAttribute')
ResetSnapshotAttribute = Action('ResetSnapshotAttribute')
RestoreAddressToClassic = Action('RestoreAddressToClassic')
RevokeSecurityGroupEgress = Action('RevokeSecurityGroupEgress')
RevokeSecurityGroupIngress = Action('RevokeSecurityGroupIngress')
RunInstances = Action('RunInstances')
RunScheduledInstances = Action('RunScheduledInstances')
StartInstances = Action('StartInstances')
StopInstances = Action('StopInstances')
TerminateInstances = Action('TerminateInstances')
UnassignPrivateIpAddresses = Action('UnassignPrivateIpAddresses')
UnmonitorInstances = Action('UnmonitorInstances')
UpdateSecurityGroupRuleDescriptionsEgress = \
    Action('UpdateSecurityGroupRuleDescriptionsEgress')
UpdateSecurityGroupRuleDescriptionsIngress = \
    Action('UpdateSecurityGroupRuleDescriptionsIngress')

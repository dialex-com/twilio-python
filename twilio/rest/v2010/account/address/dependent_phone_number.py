# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.base import InstanceResource
from twilio.rest.resources.base import ListResource


class DependentPhoneNumber(InstanceResource):
    """
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: phone_number
    
        The phone_number
    
    .. attribute:: lata
    
        The lata
    
    .. attribute:: rate_center
    
        The rate_center
    
    .. attribute:: latitude
    
        The latitude
    
    .. attribute:: longitude
    
        The longitude
    
    .. attribute:: region
    
        The region
    
    .. attribute:: postal_code
    
        The postal_code
    
    .. attribute:: iso_country
    
        The iso_country
    
    .. attribute:: address_requirements
    
        The address_requirements
    
    .. attribute:: beta
    
        The beta
    
    .. attribute:: capabilities
    
        The capabilities
    """
    id_key = "sid"

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super(DependentPhoneNumber, self).__init__(parent, None)


class DependentPhoneNumbers(ListResource):
    name = "DependentPhoneNumbers"
    mount_name = "dependent_phone_numbers"
    key = "dependent_phone_numbers"
    instance = DependentPhoneNumber

    def __init__(self, *args, **kwargs):
        super(DependentPhoneNumbers, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`DependentPhoneNumber`
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`DependentPhoneNumber`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`DependentPhoneNumber` using an iterator
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`DependentPhoneNumber`
        """
        return super(DependentPhoneNumbers, self).iter(**kwargs)

    def load_instance(self, data):
        """ Override because DependentPhoneNumber does not have a sid """
        instance = self.instance(self)
        instance.load(data)
        instance.load_subresources()
        return instance
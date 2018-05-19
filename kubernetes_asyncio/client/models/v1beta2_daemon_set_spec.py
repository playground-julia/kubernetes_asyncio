# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class V1beta2DaemonSetSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'min_ready_seconds': 'int',
        'revision_history_limit': 'int',
        'selector': 'V1LabelSelector',
        'template': 'V1PodTemplateSpec',
        'update_strategy': 'V1beta2DaemonSetUpdateStrategy'
    }

    attribute_map = {
        'min_ready_seconds': 'minReadySeconds',
        'revision_history_limit': 'revisionHistoryLimit',
        'selector': 'selector',
        'template': 'template',
        'update_strategy': 'updateStrategy'
    }

    def __init__(self, min_ready_seconds=None, revision_history_limit=None, selector=None, template=None, update_strategy=None):  # noqa: E501
        """V1beta2DaemonSetSpec - a model defined in Swagger"""  # noqa: E501

        self._min_ready_seconds = None
        self._revision_history_limit = None
        self._selector = None
        self._template = None
        self._update_strategy = None
        self.discriminator = None

        if min_ready_seconds is not None:
            self.min_ready_seconds = min_ready_seconds
        if revision_history_limit is not None:
            self.revision_history_limit = revision_history_limit
        self.selector = selector
        self.template = template
        if update_strategy is not None:
            self.update_strategy = update_strategy

    @property
    def min_ready_seconds(self):
        """Gets the min_ready_seconds of this V1beta2DaemonSetSpec.  # noqa: E501

        The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).  # noqa: E501

        :return: The min_ready_seconds of this V1beta2DaemonSetSpec.  # noqa: E501
        :rtype: int
        """
        return self._min_ready_seconds

    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds):
        """Sets the min_ready_seconds of this V1beta2DaemonSetSpec.

        The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).  # noqa: E501

        :param min_ready_seconds: The min_ready_seconds of this V1beta2DaemonSetSpec.  # noqa: E501
        :type: int
        """

        self._min_ready_seconds = min_ready_seconds

    @property
    def revision_history_limit(self):
        """Gets the revision_history_limit of this V1beta2DaemonSetSpec.  # noqa: E501

        The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.  # noqa: E501

        :return: The revision_history_limit of this V1beta2DaemonSetSpec.  # noqa: E501
        :rtype: int
        """
        return self._revision_history_limit

    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit):
        """Sets the revision_history_limit of this V1beta2DaemonSetSpec.

        The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.  # noqa: E501

        :param revision_history_limit: The revision_history_limit of this V1beta2DaemonSetSpec.  # noqa: E501
        :type: int
        """

        self._revision_history_limit = revision_history_limit

    @property
    def selector(self):
        """Gets the selector of this V1beta2DaemonSetSpec.  # noqa: E501

        A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :return: The selector of this V1beta2DaemonSetSpec.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this V1beta2DaemonSetSpec.

        A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :param selector: The selector of this V1beta2DaemonSetSpec.  # noqa: E501
        :type: V1LabelSelector
        """
        if selector is None:
            raise ValueError("Invalid value for `selector`, must not be `None`")  # noqa: E501

        self._selector = selector

    @property
    def template(self):
        """Gets the template of this V1beta2DaemonSetSpec.  # noqa: E501

        An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template  # noqa: E501

        :return: The template of this V1beta2DaemonSetSpec.  # noqa: E501
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1beta2DaemonSetSpec.

        An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template  # noqa: E501

        :param template: The template of this V1beta2DaemonSetSpec.  # noqa: E501
        :type: V1PodTemplateSpec
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def update_strategy(self):
        """Gets the update_strategy of this V1beta2DaemonSetSpec.  # noqa: E501

        An update strategy to replace existing DaemonSet pods with new pods.  # noqa: E501

        :return: The update_strategy of this V1beta2DaemonSetSpec.  # noqa: E501
        :rtype: V1beta2DaemonSetUpdateStrategy
        """
        return self._update_strategy

    @update_strategy.setter
    def update_strategy(self, update_strategy):
        """Sets the update_strategy of this V1beta2DaemonSetSpec.

        An update strategy to replace existing DaemonSet pods with new pods.  # noqa: E501

        :param update_strategy: The update_strategy of this V1beta2DaemonSetSpec.  # noqa: E501
        :type: V1beta2DaemonSetUpdateStrategy
        """

        self._update_strategy = update_strategy

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta2DaemonSetSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other